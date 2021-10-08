import matplotlib
import matplotlib.pyplot as plt

import os
import random
import io
import imageio
import glob
import scipy.misc
import numpy as np
from six import BytesIO
from PIL import Image, ImageDraw, ImageFont

import tensorflow as tf

from object_detection.utils import label_map_util
from object_detection.utils import config_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.utils import colab_utils
from object_detection.builders import model_builder


# dataset needs to be in TFRecord format

class FasterRCNNTrainer:
    def __init__(self):
        self.model_config = "/model_meta/faster_rcnn_inception_resnet_v2_1024x1024_coco17_tpu-8/pipeline.config"

    def train():
        model_lib_v2.eval_continuously(
            pipeline_config_path=FLAGS.pipeline_config_path,
            model_dir=FLAGS.model_dir,
            train_steps=FLAGS.num_train_steps,
            sample_1_of_n_eval_examples=FLAGS.sample_1_of_n_eval_examples,
            sample_1_of_n_eval_on_train_examples=(
                FLAGS.sample_1_of_n_eval_on_train_examples),
            checkpoint_dir=FLAGS.checkpoint_dir,
            wait_interval=300, timeout=FLAGS.eval_timeout)

