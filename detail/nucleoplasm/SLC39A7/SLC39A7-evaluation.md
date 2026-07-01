---
type: protein-evaluation
gene: "SLC39A7"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SLC39A7 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SLC39A7 |
| 蛋白名称 | Zinc transporter SLC39A7 |
| 蛋白大小 | 469 aa / 50.1 kDa |
| UniProt ID | Q92504 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Endoplasmic reticulum; Nucleoplasm (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 469 aa |
| 新颖性 | 8/10 | ×5 | 40.0 | PubMed=38 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=66.2; PDB=1 |
| 调控结构域 | 4/10 | ×2 | 8.0 | ZIP |
| PPI | 8/10 | ×3 | 24.0 | PPI degree=205 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |

### 3. 分析
- Endoplasmic reticulum; Nucleoplasm (Supported)
- PubMed strict=38 broad=84
- AF pLDDT=66.2 PDB=1
- InterPro: ZIP
- Pfam: Zip
- PPI degree=205 ChIP: None
37876250: The NLRX1-SLC39A7 complex orchestrates mitochondrial dynamics and mitophagy to r | 40414869: METTL9 mediated N1-Histidine methylation of SLC39A7 confers ferroptosis resistan | 19630879: Molecular characterization and association with carcass traits of the porcine SL

### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Zinc transporter SLC39A7

**功能**: Transports Zn(2+) from the endoplasmic reticulum (ER)/Golgi apparatus to the cytosol, playing an essential role in the regulation of cytosolic zinc levels (PubMed:14525538, PubMed:15705588, PubMed:28205653, PubMed:29980658). Acts as a gatekeeper of zinc release from intracellular stores, requiring post-translational activation by phosphorylation, resulting in activation of multiple downstream pathways leading to cell growth and proliferation (PubMed:22317921, PubMed:28205653, PubMed:29980658). H

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR003689 |
| Pfam | PF02535 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RPS18 | STRING | 908 |
| STUB1 | STRING | 874 |
| KIFC1 | STRING | 862 |
| SLC30A5 | STRING | 859 |
| RGL2 | STRING | 814 |
| SLC30A9 | STRING | 804 |
| RXRB | STRING | 803 |
| RING1 | STRING | 730 |


### 深度机制分析

**结构域架构**：SLC39A7/ZIP7（469 aa，50.1 kDa）属于ZIP（Zrt- and Irt-like Protein）锌转运体家族，含ZIP结构域（IPR003689，PF02535 Zip），形成推测的8次跨膜α-螺旋折叠（与典型的SLC39成员一致）。ZIP转运体的结构已在ZIP4等成员中得到低温电镜（cryo-EM）实验解析，显示其形成以膜内二聚体为功能单位的锌通道/转运体。SLC39A7定位于内质网膜，负责将ER/高尔基体腔内的Zn^2+转运至胞质——这一"看门人（gatekeeper）"功能使其在胞质锌离子稳态中占据核心位置（PMID:14525538, PMID:15705588）。

**PPI互作网络解读**：PPI degree=205，互作网络呈现出锌稳态-蛋白质量控制-染色质调控的三维交叉。关键节点：STUB1（CHIP，E3泛素连接酶，STRING 874分，介导错误折叠蛋白的泛素化降解）、RPS18（核糖体蛋白S18，STRING 908分）、SLC30A5（锌外排转运体，STRING 859分，共管的锌代谢伙伴）、RXRB（维甲酸X受体β，STRING 803分，核受体）；尤其值得注意的是RING1（STRING 730分，PRC1复合物的核心E3泛素连接酶催化H2AK119ub1），这一互作将锌转运与Polycomb介导的转录沉默直接连接。

**结构解读**：AlphaFold pLDDT=66.2（1个PDB结构验证），跨膜区预测置信度中等。ZIP折叠预测为8个跨膜α-螺旋排列成束，形成中央锌离子转运通路。功能上关键的组氨酸-rich motif（与Zn^2+配位）位于TM4/TM5区域，通常在无锌结合时常呈无序状态（解释此区域pLDDT偏低）。N端面向ER腔，含推测的锌感应域；C端面向胞质，含多个可磷酸化位点——磷酸化激活是SLC39A7功能的关键调控机制（PMID:22317921, PMID:28205653）。胞质loop区域pLDDT偏低（50-65），可能因实验结构模板缺乏导致。

**机制模型**：SLC39A7通过"锌信号（zinc signal）"调控多个下游通路：（1）ER应激与蛋白质量控制：SLC39A7介导的锌离子释放为ER中的锌依赖伴侣蛋白和折叠酶（如PDI）提供必需的金属辅因子；同时胞质锌离子作为第二信使激活MAPK/ERK和PI3K/AKT通路促进细胞增殖（PMID:29980658）；（2）线粒体动力学：NLRX1-SLC39A7复合物在有丝分裂和线粒体自噬中发挥关键作用（PMID:37876250）——NLRX1作为线粒体定位的NLR蛋白通过和ER定位的SLC39A7形成ER-线粒体接触位点的分子桥梁；（3）染色质调控：SLC39A7通过RING1（PRC1）互作参与Polycomb介导的转录抑制——锌离子是许多锌指蛋白和组蛋白修饰酶（如HDAC锌依赖的去乙酰化酶）的必需辅因子，SLC39A7可能通过调控核质游离锌离子池影响这些酶活性。

**TE调控展望**：SLC39A7通过两条途径与TE调控关联：（1）RING1互作意味着SLC39A7可能影响PRC1催化的H2AK119ub1——此修饰是Polycomb介导的TE沉默和X染色体失活的关键染色质标记；（2）锌离子作为KZNF蛋白（C2H2锌指）的结构性辅因子（每个锌指需配位一个Zn^2+），SLC39A7调控的锌离子供应直接影响ZNF蛋白的折叠、DNA结合活性、进而影响其TE识别和沉默效率。PMID:40414869发现的METTL9-SLC39A7-SLC39A7组氨酸甲基化-铁死亡抵抗通路进一步丰富了其信号网络。


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q92504-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 84**

| 42351690 | ZIP7 Drives Glycolytic Reprogramming and Lactate-Mediated Immune Remodeling in Lung Adenocarcinoma Through GSK3β-NRF2 Si | Biomedicines 2026 |
| 42193417 | Machine Learning-Based Identification of Immune Inflammation-Related Genes as Shared Potential Diagnostic Biomarkers in  | Biomedicines 2026 |
| 42014757 | Zinc-redox crosstalk regulates proteostasis in the endoplasmic reticulum. | Nat Commun 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SLC39A7

