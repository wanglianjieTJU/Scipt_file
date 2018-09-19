import sys
import argparse
from xml.dom.minidom import Document
import cv2, os
import glob
import xml.etree.ElementTree as ET
import shutil
import numpy as np
global  truncation

def generate_xml(name, lines, img_size=(960, 1280, 3), \
                 class_sets=(
                 'Pedestrain', 'people', 'bicycle', 'car', 'Van', 'Truck', 'tricycle', 'van-like-tricycle', 'others',
                 'Bus', 'motor', 'ignored'), \
                 doncateothers=True):
    doc = Document()

    def append_xml_node_attr(child, parent=None, text=None):
        ele = doc.createElement(child)
        if not text is None:
            text_node = doc.createTextNode(text)
            ele.appendChild(text_node)
        parent = doc if parent is None else parent
        parent.appendChild(ele)
        return ele

    img_name = name + '.jpg'

    # create header
    annotation = append_xml_node_attr('annotation')
    append_xml_node_attr('folder', parent=annotation, text='UAV')
    append_xml_node_attr('filename', parent=annotation, text=img_name)
    source = append_xml_node_attr('source', parent=annotation)
    append_xml_node_attr('database', parent=source, text='UAV')
    append_xml_node_attr('annotation', parent=source, text='UAV')
    append_xml_node_attr('image', parent=source, text='UAV')
    append_xml_node_attr('flickrid', parent=source, text='000000')
    owner = append_xml_node_attr('owner', parent=annotation)
    append_xml_node_attr('url', parent=owner, text='UAV')
    size = append_xml_node_attr('size', annotation)
    append_xml_node_attr('width', size, str(img_size[1]))
    append_xml_node_attr('height', size, str(img_size[0]))
    append_xml_node_attr('depth', size, str(img_size[2]))
    append_xml_node_attr('segmented', parent=annotation, text='0')

    # create objects
    objs = []
    for line in lines:
        splitted_line = line.strip().lower().split()
        cls = splitted_line[1].lower()
        # if cls == ' Pedestrain':
        #     cls = 'Pedestrain'
        # if not doncateothers and cls not in class_sets:
        #     continue
        # cls = 'dontcare' if cls not in class_sets else cls

        obj = append_xml_node_attr('object', parent=annotation)
        if splitted_line[0]=='ignored':
            cls=splitted_line[0]
            x1, y1, x2, y2 = int(splitted_line[1]), int(splitted_line[2]), int(splitted_line[3]), int(splitted_line[4])

            append_xml_node_attr('name', parent=obj, text=str(cls))
            append_xml_node_attr('occlusion', parent=obj, text=str(0))
            append_xml_node_attr('truncated', parent=obj, text=str(0))
            append_xml_node_attr('difficult', parent=obj, text=str(int(0)))
            bb = append_xml_node_attr('bndbox', parent=obj)
            append_xml_node_attr('xmin', parent=bb, text=str(x1))
            append_xml_node_attr('ymin', parent=bb, text=str(y1))
            append_xml_node_attr('xmax', parent=bb, text=str(x2))
            append_xml_node_attr('ymax', parent=bb, text=str(y2))
        else:
            occlusion = int(splitted_line[2])
            #        x1, y1, x2, y2 = int(float(splitted_line[4]) + 1), int(float(splitted_line[5]) + 1), \
            #                         int(float(splitted_line[6]) + 1), int(float(splitted_line[7]) + 1)
            x1, y1, x2, y2 = int(splitted_line[4]), int(splitted_line[5]), int(splitted_line[6]), int(splitted_line[7])
            truncation = int(splitted_line[3])
            difficult = 1 if _is_hard(cls, truncation, occlusion, x1, y1, x2, y2) else 0
            truncted = 0 if truncation <= 1 else 1
            if splitted_line[1]=='pedestrain':
                cls='pedestrian'
            append_xml_node_attr('name', parent=obj, text=cls)
            append_xml_node_attr('occlusion', parent=obj, text=str(occlusion))
            append_xml_node_attr('truncated', parent=obj, text=str(truncted))
            append_xml_node_attr('difficult', parent=obj, text=str(int(difficult)))
            bb = append_xml_node_attr('bndbox', parent=obj)
            append_xml_node_attr('xmin', parent=bb, text=str(x1))
            append_xml_node_attr('ymin', parent=bb, text=str(y1))
            append_xml_node_attr('xmax', parent=bb, text=str(x2))
            append_xml_node_attr('ymax', parent=bb, text=str(y2))

    o = {'class': cls, 'box': np.asarray([x1, y1, x2, y2], dtype=int), \
         'truncation': truncation, 'difficult': difficult, 'occlusion': occlusion}
    objs.append(o)

    return doc, objs


def _is_hard(cls, truncation, occlusion, x1, y1, x2, y2):
    hard = False
    if y2 - y1 < 25 and occlusion >= 1:
        hard = True
        return hard
    if occlusion >=1:
        hard = True
        return hard
    if truncation >=1:
        hard = True
        return hard
    return hard


def parse_args():
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser(description='Convert UAV dataset into Pascal voc format')
    parser.add_argument('--UAV', dest='UAV',
                        help='path to data root',
                        default='./test_P', type=str)
    parser.add_argument('--out', dest='outdir',
                        help='path to voc-UAV',
                        default='./test_3x', type=str)
    parser.add_argument('--draw', dest='draw',
                        help='draw rects on images',
                        default=0, type=int)
    parser.add_argument('--dontcareothers', dest='dontcareothers',
                        help='ignore other categories, add them to dontcare rsgions',
                        default=1, type=int)

    if len(sys.argv) == 1:
        parser.print_help()
        # sys.exit(1)
    args = parser.parse_args()
    return args


def build_voc_dirs(outdir):
    """
    Build voc dir structure:
        VOC2007
            |-- Annotations
                    |-- ***.xml
            |-- ImageSets
                    |-- Layout
                            |-- [test|train|trainval|val].txt
                    |-- Main
                            |-- class_[test|train|trainval|val].txt
                    |-- Segmentation
                            |-- [test|train|trainval|val].txt
            |-- JPEGImages
                    |-- ***.jpg
            |-- SegmentationClass
                    [empty]
            |-- SegmentationObject
                    [empty]
    """
    mkdir = lambda dir: os.makedirs(dir) if not os.path.exists(dir) else None
    mkdir(outdir)
    mkdir(os.path.join(outdir, 'Annotations'))
    mkdir(os.path.join(outdir, 'ImageSets'))
    mkdir(os.path.join(outdir, 'ImageSets', 'Layout'))
    mkdir(os.path.join(outdir, 'ImageSets', 'Main'))
    mkdir(os.path.join(outdir, 'ImageSets', 'Segmentation'))
    mkdir(os.path.join(outdir, 'JPEGImages'))
    mkdir(os.path.join(outdir, 'SegmentationClass'))
    mkdir(os.path.join(outdir, 'SegmentationObject'))

    return os.path.join(outdir, 'Annotations'), os.path.join(outdir, 'JPEGImages'), os.path.join(outdir, 'ImageSets',
                                                                                                 'Main')


# def _draw_on_image(img, objs, class_sets_dict):
#    colors = [(86, 0, 240), (173, 225, 61), (54, 137, 255),\
#              (151, 0, 255), (243, 223, 48), (0, 117, 255),\
#              (58, 184, 14), (86, 67, 140), (121, 82, 6),\
#              (174, 29, 128), (115, 154, 81), (86, 255, 234)]
#    font = cv2.FONT_HERSHEY_SIMPLEX
#    for ind, obj in enumerate(objs):
#        if obj['box'] is None: continue
#        x1, y1, x2, y2 = obj['box'].astype(int)
#        cls_id = class_sets_dict[obj['class']]
#        if obj['class'] == 'dontcare':
#            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 1)
#            continue
#        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), colors[cls_id % len(colors)], 1)
#        text = '{:s}*|'.format(obj['class'][:3]) if obj['difficult'] == 1 else '{:s}|'.format(obj['class'][:3])
#        text += '{:.1f}|'.format(obj['truncation'])
#        text += str(obj['occlusion'])
#        cv2.putText(img, text, (x1-2, y2-2), font, 0.5, (255, 0, 255), 1)
#    return img


if __name__ == '__main__':
    args = parse_args()

    _kittidir = args.UAV
    _outdir = args.outdir
    _draw = bool(args.draw)
    _dest_label_dir, _dest_img_dir, _dest_set_dir = build_voc_dirs(_outdir)
    _doncateothers = bool(args.dontcareothers)

    for dset in ['train']:

        _labeldir = os.path.join('./test_x2')
        _imagedir = os.path.join('./test_P')

        class_sets = ('Pedestrain','people', 'bicycle', 'car', 'Van', 'Truck', 'tricycle','van-like-tricycle','others', 'Bus','motor','ignored')

        # class_sets = ('pedestrain', 'cyclist', 'car', 'bus', 'truck','van') Pedestrain

        class_sets_dict = dict((k, i) for i, k in enumerate(class_sets))
        allclasses = {}
        fs = [open(os.path.join(_dest_set_dir, cls + '_' + dset + '.txt'), 'w') for cls in class_sets]
        ftrain = open(os.path.join(_dest_set_dir, dset + '.txt'), 'w')

        files = glob.glob(os.path.join(_labeldir, '*.txt'))
        files.sort()
        for file in files:
            path, basename = os.path.split(file)
            stem, ext = os.path.splitext(basename)
            with open(file, 'r') as f:
                lines = f.readlines()
            img_file = os.path.join(_imagedir, stem + '.jpg')
            img = cv2.imread(img_file)
            img_size = img.shape

            doc, objs = generate_xml(stem, lines, img_size, class_sets=class_sets, doncateothers=_doncateothers)
            #            if _draw:
            #                _draw_on_image(img, objs, class_sets_dict)

            cv2.imwrite(os.path.join(_dest_img_dir, stem + '.jpg'), img)
            xmlfile = os.path.join(_dest_label_dir, stem + '.xml')
            with open(xmlfile, 'w') as f:
                f.write(doc.toprettyxml(indent='	'))

            ftrain.writelines(stem + '\n')

            # build [cls_train.txt]import sys
import argparse
from xml.dom.minidom import Document
import cv2, os
import glob
import xml.etree.ElementTree as ET
import shutil
import numpy as np
global  truncation

def generate_xml(name, lines, img_size=(960, 1280, 3), \
                 class_sets=(
                 'Pedestrain', 'people', 'bicycle', 'car', 'Van', 'Truck', 'tricycle', 'van-like-tricycle', 'others',
                 'Bus', 'motor', 'ignored'), \
                 doncateothers=True):
    doc = Document()

    def append_xml_node_attr(child, parent=None, text=None):
        ele = doc.createElement(child)
        if not text is None:
            text_node = doc.createTextNode(text)
            ele.appendChild(text_node)
        parent = doc if parent is None else parent
        parent.appendChild(ele)
        return ele

    img_name = name + '.jpg'

    # create header
    annotation = append_xml_node_attr('annotation')
    append_xml_node_attr('folder', parent=annotation, text='UAV')
    append_xml_node_attr('filename', parent=annotation, text=img_name)
    source = append_xml_node_attr('source', parent=annotation)
    append_xml_node_attr('database', parent=source, text='UAV')
    append_xml_node_attr('annotation', parent=source, text='UAV')
    append_xml_node_attr('image', parent=source, text='UAV')
    append_xml_node_attr('flickrid', parent=source, text='000000')
    owner = append_xml_node_attr('owner', parent=annotation)
    append_xml_node_attr('url', parent=owner, text='UAV')
    size = append_xml_node_attr('size', annotation)
    append_xml_node_attr('width', size, str(img_size[1]))
    append_xml_node_attr('height', size, str(img_size[0]))
    append_xml_node_attr('depth', size, str(img_size[2]))
    append_xml_node_attr('segmented', parent=annotation, text='0')

    # create objects
    objs = []
    for line in lines:
        splitted_line = line.strip().lower().split()
        cls = splitted_line[1].lower()
        # if cls == ' Pedestrain':
        #     cls = 'Pedestrain'
        # if not doncateothers and cls not in class_sets:
        #     continue
        # cls = 'dontcare' if cls not in class_sets else cls

        obj = append_xml_node_attr('object', parent=annotation)
        if splitted_line[0]=='ignored':
            x1, y1, x2, y2 = int(splitted_line[1]), int(splitted_line[2]), int(splitted_line[3]), int(splitted_line[4])
            bb = append_xml_node_attr('bndbox', parent=obj)
            append_xml_node_attr('xmin', parent=bb, text=str(x1))
            append_xml_node_attr('ymin', parent=bb, text=str(y1))
            append_xml_node_attr('xmax', parent=bb, text=str(x2))
            append_xml_node_attr('ymax', parent=bb, text=str(y2))
        else:
            occlusion = int(splitted_line[2])
            #        x1, y1, x2, y2 = int(float(splitted_line[4]) + 1), int(float(splitted_line[5]) + 1), \
            #                         int(float(splitted_line[6]) + 1), int(float(splitted_line[7]) + 1)
            x1, y1, x2, y2 = int(splitted_line[4]), int(splitted_line[5]), int(splitted_line[6]), int(splitted_line[7])
            truncation = int(splitted_line[3])
            difficult = 1 if _is_hard(cls, truncation, occlusion, x1, y1, x2, y2) else 0
            truncted = 0 if truncation <= 1 else 1
            if splitted_line[1]=='pedestrain':
                cls='pedestrian'
            append_xml_node_attr('name', parent=obj, text=cls)
            append_xml_node_attr('occlusion', parent=obj, text=str(occlusion))
            append_xml_node_attr('truncated', parent=obj, text=str(truncted))
            append_xml_node_attr('difficult', parent=obj, text=str(int(difficult)))
            bb = append_xml_node_attr('bndbox', parent=obj)
            append_xml_node_attr('xmin', parent=bb, text=str(x1))
            append_xml_node_attr('ymin', parent=bb, text=str(y1))
            append_xml_node_attr('xmax', parent=bb, text=str(x2))
            append_xml_node_attr('ymax', parent=bb, text=str(y2))

    o = {'class': cls, 'box': np.asarray([x1, y1, x2, y2], dtype=int), \
         'truncation': truncation, 'difficult': difficult, 'occlusion': occlusion}
    objs.append(o)

    return doc, objs


def _is_hard(cls, truncation, occlusion, x1, y1, x2, y2):
    hard = False
    if y2 - y1 < 25 and occlusion >= 2:
        hard = True
        return hard
    if occlusion >=1:
        hard = True
        return hard
    if truncation >=1:
        hard = True
        return hard
    return hard


def parse_args():
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser(description='Convert UAV dataset into Pascal voc format')
    parser.add_argument('--UAV', dest='UAV',
                        help='path to data root',
                        default='./test_P', type=str)
    parser.add_argument('--out', dest='outdir',
                        help='path to voc-UAV',
                        default='./test_3x', type=str)
    parser.add_argument('--draw', dest='draw',
                        help='draw rects on images',
                        default=0, type=int)
    parser.add_argument('--dontcareothers', dest='dontcareothers',
                        help='ignore other categories, add them to dontcare rsgions',
                        default=1, type=int)

    if len(sys.argv) == 1:
        parser.print_help()
        # sys.exit(1)
    args = parser.parse_args()
    return args


def build_voc_dirs(outdir):
    """
    Build voc dir structure:
        VOC2007
            |-- Annotations
                    |-- ***.xml
            |-- ImageSets
                    |-- Layout
                            |-- [test|train|trainval|val].txt
                    |-- Main
                            |-- class_[test|train|trainval|val].txt
                    |-- Segmentation
                            |-- [test|train|trainval|val].txt
            |-- JPEGImages
                    |-- ***.jpg
            |-- SegmentationClass
                    [empty]
            |-- SegmentationObject
                    [empty]
    """
    mkdir = lambda dir: os.makedirs(dir) if not os.path.exists(dir) else None
    mkdir(outdir)
    mkdir(os.path.join(outdir, 'Annotations'))
    mkdir(os.path.join(outdir, 'ImageSets'))
    mkdir(os.path.join(outdir, 'ImageSets', 'Layout'))
    mkdir(os.path.join(outdir, 'ImageSets', 'Main'))
    mkdir(os.path.join(outdir, 'ImageSets', 'Segmentation'))
    mkdir(os.path.join(outdir, 'JPEGImages'))
    mkdir(os.path.join(outdir, 'SegmentationClass'))
    mkdir(os.path.join(outdir, 'SegmentationObject'))

    return os.path.join(outdir, 'Annotations'), os.path.join(outdir, 'JPEGImages'), os.path.join(outdir, 'ImageSets',
                                                                                                 'Main')


# def _draw_on_image(img, objs, class_sets_dict):
#    colors = [(86, 0, 240), (173, 225, 61), (54, 137, 255),\
#              (151, 0, 255), (243, 223, 48), (0, 117, 255),\
#              (58, 184, 14), (86, 67, 140), (121, 82, 6),\
#              (174, 29, 128), (115, 154, 81), (86, 255, 234)]
#    font = cv2.FONT_HERSHEY_SIMPLEX
#    for ind, obj in enumerate(objs):
#        if obj['box'] is None: continue
#        x1, y1, x2, y2 = obj['box'].astype(int)
#        cls_id = class_sets_dict[obj['class']]
#        if obj['class'] == 'dontcare':
#            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 1)
#            continue
#        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), colors[cls_id % len(colors)], 1)
#        text = '{:s}*|'.format(obj['class'][:3]) if obj['difficult'] == 1 else '{:s}|'.format(obj['class'][:3])
#        text += '{:.1f}|'.format(obj['truncation'])
#        text += str(obj['occlusion'])
#        cv2.putText(img, text, (x1-2, y2-2), font, 0.5, (255, 0, 255), 1)
#    return img


if __name__ == '__main__':
    args = parse_args()

    _kittidir = args.UAV
    _outdir = args.outdir
    _draw = bool(args.draw)
    _dest_label_dir, _dest_img_dir, _dest_set_dir = build_voc_dirs(_outdir)
    _doncateothers = bool(args.dontcareothers)

    for dset in ['train']:

        _labeldir = os.path.join('./test_x2')
        _imagedir = os.path.join('./test_P')

        class_sets = ('Pedestrain','people', 'bicycle', 'car', 'Van', 'Truck', 'tricycle','van-like-tricycle','others', 'Bus','motor','ignored')

        # class_sets = ('pedestrain', 'cyclist', 'car', 'bus', 'truck','van') Pedestrain

        class_sets_dict = dict((k, i) for i, k in enumerate(class_sets))
        allclasses = {}
        fs = [open(os.path.join(_dest_set_dir, cls + '_' + dset + '.txt'), 'w') for cls in class_sets]
        ftrain = open(os.path.join(_dest_set_dir, dset + '.txt'), 'w')

        files = glob.glob(os.path.join(_labeldir, '*.txt'))
        files.sort()
        for file in files:
            path, basename = os.path.split(file)
            stem, ext = os.path.splitext(basename)
            with open(file, 'r') as f:
                lines = f.readlines()
            img_file = os.path.join(_imagedir, stem + '.jpg')
            img = cv2.imread(img_file)
            img_size = img.shape

            doc, objs = generate_xml(stem, lines, img_size, class_sets=class_sets, doncateothers=_doncateothers)
            #            if _draw:
            #                _draw_on_image(img, objs, class_sets_dict)

            cv2.imwrite(os.path.join(_dest_img_dir, stem + '.jpg'), img)
            xmlfile = os.path.join(_dest_label_dir, stem + '.xml')
            with open(xmlfile, 'w') as f:
                f.write(doc.toprettyxml(indent='	'))

            ftrain.writelines(stem + '\n')

            # build [cls_train.txt]
            # Car_train.txt: 0000xxx [1 | -1]
            cls_in_image = set([o['class'] for o in objs])

            for obj in objs:
                cls = obj['class']
                allclasses[cls] = 0 \
                    if not cls in allclasses.keys() else allclasses[cls] + 1

            for cls in cls_in_image:
                if cls in class_sets:
                    fs[class_sets_dict[cls]].writelines(stem + ' 1\n')
            for cls in class_sets:
                if cls not in cls_in_image:
                    fs[class_sets_dict[cls]].writelines(stem + ' -1\n')

                    #            if int(stem) % 100 == 0:
            print(file)

        (f.close() for f in fs)
        ftrain.close()

        print '~~~~~~~~~~~~~~~~~~~'
        print allclasses
        print '~~~~~~~~~~~~~~~~~~~'
        shutil.copyfile(os.path.join(_dest_set_dir, 'train.txt'), os.path.join(_dest_set_dir, 'val.txt'))
        shutil.copyfile(os.path.join(_dest_set_dir, 'train.txt'), os.path.join(_dest_set_dir, 'trainval.txt'))
        for cls in class_sets:
            shutil.copyfile(os.path.join(_dest_set_dir, cls + '_train.txt'),
                            os.path.join(_dest_set_dir, cls + '_trainval.txt'))
            shutil.copyfile(os.path.join(_dest_set_dir, cls + '_train.txt'),
                            os.path.join(_dest_set_dir, cls + '_val.txt'))
