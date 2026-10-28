# MPI 讲义图片来源与许可说明

本目录中的课程原创文字、代码和自绘示意图适用仓库的 [MIT License](../../../../../%E8%AF%BE%E7%A8%8B/%E5%B9%B6%E8%A1%8C%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%A1%E7%AE%97/LICENSE)。以下第三方图片保留各自的来源、署名和许可条件，不因随课程仓库发布而改用 MIT 许可。讲义及 PDF 课件末尾同时保留图片参考文献。

## 第一讲：第三方图片

| 文件 | 作者与来源 | 许可或复用依据 | 本课程使用方式 |
| --- | --- | --- | --- |
| [nersc-racks-cc0.jpg](../../../../../04_Assets/Images/Courses/%E5%B9%B6%E8%A1%8C%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%A1%E7%AE%97/PPT/mpi/01-%E8%83%8C%E6%99%AF%E4%B8%8E%E7%A1%AC%E4%BB%B6%E6%9E%B6%E6%9E%84/assets/nersc-racks-cc0.jpg) | Derrick Coetzee，[Front of server racks at NERSC](https://commons.wikimedia.org/wiki/File:Front_of_server_racks_at_NERSC.jpg)，Wikimedia Commons | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | 原照片；课件封面按版式裁切显示 |
| [cray-1-museum-cc-by-sa.jpg](../../../../../04_Assets/Images/Courses/%E5%B9%B6%E8%A1%8C%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%A1%E7%AE%97/PPT/mpi/01-%E8%83%8C%E6%99%AF%E4%B8%8E%E7%A1%AC%E4%BB%B6%E6%9E%B6%E6%9E%84/assets/cray-1-museum-cc-by-sa.jpg) | Jud McCranie，[Cray-1 at Computer Museum of America](https://commons.wikimedia.org/wiki/File:Cray-1_at_Computer_Museum_of_America.jpg)，Wikimedia Commons | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) | 照片未修改，保留作者与许可署名 |
| [aspect-2012-fig8-temperature.png](../../../../../04_Assets/Images/Courses/%E5%B9%B6%E8%A1%8C%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%A1%E7%AE%97/PPT/mpi/01-%E8%83%8C%E6%99%AF%E4%B8%8E%E7%A1%AC%E4%BB%B6%E6%9E%B6%E6%9E%84/assets/aspect-2012-fig8-temperature.png)；[aspect-2012-fig8-partition.png](../../../../../04_Assets/Images/Courses/%E5%B9%B6%E8%A1%8C%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%A1%E7%AE%97/PPT/mpi/01-%E8%83%8C%E6%99%AF%E4%B8%8E%E7%A1%AC%E4%BB%B6%E6%9E%B6%E6%9E%84/assets/aspect-2012-fig8-partition.png) | Kronbichler, M., Heister, T., & Bangerth, W. (2012). *High accuracy mantle convection simulation through modern numerical methods*. *Geophysical Journal International*, 191(1), 12–29，[正式发表版 Fig. 8](https://academic.oup.com/gji/article/191/1/12/585193) | 按[期刊教学复用说明](https://academic.oup.com/gji/pages/rights_and_new_business_development)在完整注明出处的条件下用于教学；不宣称图像为 MIT 或其他开放许可 | 两个原图面板从[作者公开稿](https://www.sci.utah.edu/~heister/preprints/mantle_conv.pdf)第 15 页 Fig. 6 无改动提取，对应正式发表版 Fig. 8；完整提取说明见 [ASPECT 原图来源](01-%E8%83%8C%E6%99%AF%E4%B8%8E%E7%A1%AC%E4%BB%B6%E6%9E%B6%E6%9E%84/assets/aspect-2012-fig8-SOURCE.md) |

ASPECT 的两幅原图展示同一次三维球壳模拟的温度等值面与处理器网格分区。二维网格分区示意图为本课程自行绘制，与原论文图像分别列明。

## 课程自绘图

- 课程导览 `first-day-hangout/`：PDF 内的学习路线、课程位置和网格分区 TikZ 图，依据任课教师确认的教学安排与 MPI 概念；网格图为原理示意。
- 第一讲：`hardware-hierarchy.svg`、`rank-placement.svg`、`programming-models.svg`、`git-workflow.svg`、`aspect-mesh-partition.svg` 及后者用于排版的 PNG 版本；新增 [image-tiles-parallel.svg](../../../../../04_Assets/Images/Courses/%E5%B9%B6%E8%A1%8C%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%A1%E7%AE%97/PPT/mpi/01-%E8%83%8C%E6%99%AF%E4%B8%8E%E7%A1%AC%E4%BB%B6%E6%9E%B6%E6%9E%84/assets/image-tiles-parallel.svg) 展示图像分块、本地处理与并行输出。
- 第二讲：`spmd-flow.svg`、`world-ranks.svg`，以及 PDF 课件中的 TikZ 示意图。

自绘图用于解释课程概念，不表示某一具体机器的实物布线。各目录的 `封面预览.png` 是对应 PDF 封面的预览；课程导览封面为课程自绘，第一讲预览含上述 NERSC 照片。

## 来源记录

本说明依据随原讲义保留的图片参考文献与 [ASPECT 图像提取记录](01-%E8%83%8C%E6%99%AF%E4%B8%8E%E7%A1%AC%E4%BB%B6%E6%9E%B6%E6%9E%84/assets/aspect-2012-fig8-SOURCE.md)整理。原讲义的资料核对日期：第一讲 2026-09-27，第二讲 2026-10-11；新增图像分块案例依据第一讲参考文献第 22 项，核对日期为 2026-10-11。复用第三方图片时，请继续保留署名，并按各自许可或权利方复用条件处理。
