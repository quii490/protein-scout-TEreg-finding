---
type: protein-evaluation
gene: "CNTD2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CNTD2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CNTD2 |
| 蛋白名称 | Cyclin-P |
| 蛋白大小 | 307 aa / 33.6 kDa |
| UniProt ID | Q9H8S5 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 307 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=7 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=70.7; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Cyclin; Cyclin-like_dom; Cyclin-like_sf |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **117/180** | |
| **归一化总分** | | | **65.0/100** | 互证: +2 |

### 3. 分析
- HPA: nan (nan)
- PubMed: strict=7, broad=8
- AF pLDDT: 70.7 / PDB: 0
- InterPro: Cyclin; Cyclin-like_dom; Cyclin-like_sf
- Pfam: Cyclin_N
- PPI degree=0 / ChIP: None
29176782: A universal mammalian vaccine cell line substrate. | 30087414: The atypical cyclin CNTD2 promotes colon cancer cell proliferation and migration | 33613629: Enhanced Expression of CNTD2/CCNP Predicts Poor Prognosis in Bladder Cancer Base

### 4. 总体评价
**65.0/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Cyclin-P

**功能**: Seems to be involved in the regulation of proliferation and migration

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR039361 |
| InterPro | IPR013763 |
| InterPro | IPR036915 |
| InterPro | IPR006671 |
| Pfam | PF00134 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CDK2 | STRING | 813 |
| CCNA2 | STRING | 769 |
| CCNA1 | STRING | 765 |
| CDC2 | STRING | 761 |
| CDK1 | STRING | 761 |
| CDC20 | STRING | 752 |
| CDC20B | STRING | 752 |



### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CNTD2

### PubMed

**Count: 8**

| PMID | Title |
|---|---|
| 41203638 | Opposite regulation of immune genes in blood and skin highlights tissue-specific dynamics of mpox virus. |
| 34604945 | Atypical cyclin P regulates cancer cell stemness through activation of the WNT pathway. |
| 33613629 | Enhanced Expression of CNTD2/CCNP Predicts Poor Prognosis in Bladder Cancer Based on the GSE13507. |
| 30087414 | The atypical cyclin CNTD2 promotes colon cancer cell proliferation and migration. |
| 29176782 | A universal mammalian vaccine cell line substrate. |

### 深度机制分析

CNTD2/Cyclin-P（UniProt Q9H8S5）属于非典型细胞周期蛋白（atypical cyclin）家族，其N端含有保守的Cyclin_N结构域（PF00134），对应InterPro条目IPR039361（Cyclin-P）、IPR013763（Cyclin-like_dom）和IPR036915（Cyclin-like_sf）。经典的细胞周期蛋白采用由5个alpha螺旋组成的紧凑cyclin box折叠，通过一个保守的疏水沟槽结合并激活CDK激酶。然而，CNTD2被归类为"非典型"cyclin，其cyclin box序列与典型cyclins（如CCNA/B/D/E）的相似性有限，暗示其可能采用差异化的CDK结合模式或具有不依赖CDK的独立功能。AlphaFold v6预测pLDDT=70.7，无实验PDB结构，Cyclin_N区域的预测置信度中等，提示cyclin box折叠部分稳定但存在柔性环区。

PPI分析显示CNTD2与核心细胞周期调控因子的互作富集：CDK2（STRING=813）、CCNA2（769）、CDK1/CDC2（761）、CCNA1（765）和CDC20（752）均为STRING预测但缺乏直接实验验证。这种模式与非典型cyclin的已知行为一致——它们通常不与经典CDK形成稳定复合物，而是通过瞬时、低亲和力的互作调控CDK活性或作为CDK非依赖的转录调控因子。功能研究表明CNTD2促进结肠癌细胞增殖和迁移（PMID:30087414），并在膀胱癌中作为不良预后标志物高表达（PMID:33613629），最有趣的机制线索来自CNTD2通过激活WNT通路调控癌症干细胞干性（PMID:34604945），提示其功能超出了经典细胞周期调控范畴。

HPA定位信息有限（nan），但总体评估标记为nucleoplasm，结合其与CDK的预测互作和cyclin box结构域的存在，核质定位符合其作为细胞周期调控因子的功能预期。若CNTD2通过WNT通路发挥作用，其核内功能可能与beta-catenin/TCF转录复合物的调控相关——许多非典型cyclins（如CCNK/Cyclin-K与CDK12/13协同磷酸化RNA Pol II CTD）在转录调控中扮演关键角色。

CNTD2的研究新颖性极高（PubMed strict=7），仅有3篇癌症功能研究进行直接功能表征，结构生物学和生化机制几乎完全空白。对于TE调控研究，Cyclin/CDK通路与转座元件沉默的关联主要经由RB-E2F通路（E2F调控LINE-1转录）和DREAM复合体。若CNTD2确实作为一个CDK激活因子在核内参与WNT信号调控，其可能通过影响TCF/LEF靶基因的转录程序间接参与TE表达调控——WNT通路在结直肠癌中激活的LINE-1和ERV转录已被文献记录。然而，目前缺乏CNTD2的ChIP-seq、RNA-seq或蛋白质组学数据，其靶标谱和分子机制均需从头解析。

### 5. 数据来源
（以下为原报告尾部内容）

### 补充分析 (UniProt API)
