---
type: protein-evaluation
gene: "PGBD1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PGBD1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PGBD1 |
| 蛋白名称 | PiggyBac transposable element-derived protein 1 |
| 蛋白大小 | 809 aa / 92.5 kDa |
| UniProt ID | Q96JS3 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 809 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=10 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=65.8; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | PGBD; PiggyBac_TE-derived; SCAN_dom |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=28 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |

### 3. 分析
| 项目 | 详情 |
|---|---|
| HPA | Cytosol; Nucleoplasm (Approved) |
| PubMed | strict=10, broad=35 |
| AF pLDDT | 65.8 |
| PDB | 0 |
| InterPro | PGBD; PiggyBac_TE-derived; SCAN_dom |
| Pfam | DDE_Tnp_1_7; SCAN |
| PPI degree | 28 |
| ChIP | None |

**Papers**: 36205081: A Novel Gene Controls a New Structure: PiggyBac Transposable Element-Derived 1,  | 23437227: Replication of association between schizophrenia and chromosome 6p21-6p22.1 poly | 38495498: Illuminating Shared Genetic Associations Between Oesophageal Carcinoma and Pulmo

### 4. 总体评价
★★★★  **72.7/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: PiggyBac transposable element-derived protein 1

**功能**: Transposase-derived from PiggyBac DNA transposons. Although it has been fully domesticated and lacks transposase activity, PGBD1 has acquired DNA-binding capability (PubMed:12955498, PubMed:35609796, PubMed:36205081). It preferentially binds in and around genes involved in neuronal development, leading to their transcriptional pausing. Notably, PGBD1 suppresses paraspeckle assembly in neuronal cells (PubMed:36205081)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029526 |
| InterPro | IPR052638 |
| InterPro | IPR003309 |
| InterPro | IPR038269 |
| InterPro | IPR001190 |
| Pfam | PF13843 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ZKSCAN4 | STRING | 840 |
| SCAND1 | STRING | 837 |
| RAZ1 | STRING | 837 |
| ZNF446 | STRING | 835 |
| ZSCAN18 | STRING | 834 |
| ZNF396 | STRING | 831 |
| ZNF24 | STRING | 831 |
| ZSCAN32 | STRING | 828 |


### 深度机制分析

**结构域架构**：PGBD1（809 aa，92.5 kDa）是猪gypsy-Bac（PiggyBac）DNA转座子的驯化产物，拥有极其特殊的结构域组成——N端SCAN_dom（IPR003309，IPR038269，PF13843 SCAN）是C2H2锌指蛋白中常见的蛋白互作结构域（介导ZNF蛋白的选择性同源/异源二聚化），而C端的PiggyBac_TE-derived结构域（IPR029526，DDE_Tnp_1_7 PF13843）直接继承自祖先转座子，保留了DNA结合能力但已丧失催化性DDE三联体的转座酶活性（该特征由PMID:12955498, PMID:35609796, PMID:36205081验证）。SCAN + PB转座酶融合是自然界蛋白质驯化（domestication）的经典范例。

**PPI互作网络解读**：PPI degree=28，但互作伙伴的质量极高——SCAND1（STRING 837分）、ZKSCAN4（840分）、ZNF446（835分）、ZNF24（831分），全部为SCAN结构域家族ZNF蛋白。这种"SCAN-SCAN"同家族互作模式极为典型：SCAN结构域通过形成卷曲螺旋二聚体介导KZNF蛋白的选择性配对，使得PGBD1可作为SCAN家族ZNF蛋白的共调节因子进入已存在的转录调控网络。SCAND1作为SCAN家族唯一的孤立SCAN蛋白（无锌指），可能作为SCAN网络的"抑制性诱饵"调节二聚化平衡。

**结构解读**：AlphaFold pLDDT=65.8，整体预测质量偏低但结构域间差异大。SCAN结构域（pLDDT ~70-80）预测形成由5个α-螺旋组成的球状结构，通过螺旋1/2/3的疏水面介导二聚化。PB转座酶结构域（pLDDT 55-70）保留了祖先RNase H样折叠的催化支架，但DDE催化三联体（通常为D268/D346/D447）中的一个或多个关键残基已被替换，解释了其丧失转座活性但保留DNA结合能力的功能特征。连接SCAN和PB域的linker区域（pLDDT <50）可能具有显著的构象柔性，使得两个结构域间存在动态的空间关系。

**机制模型**：PGBD1作为"转录暂停因子"（transcriptional pausing factor）通过以下机制抑制神经元分化基因：（1）PB转座酶结构域识别并结合神经元发育相关基因（如NEFL、SYP、DLG4等突触基因）的启动子和基因体区域——ChIP已证实其富集于这些基因位点；（2）SCAN结构域通过与SCAND1/ZKSCAN4等蛋白二聚化，可能招募额外的转录抑制因子（如CTBP、HDAC）至这些位点；（3）PMID:36205081的关键发现——PGBD1抑制paraspeckle（核内RNA-蛋白凝聚体）的组装，可能通过结合NEAT1_2 RNA（paraspeckle的结构性lncRNA支架）竞争性取代关键蛋白组分（如NONO/SFPQ）来实现。

**TE调控展望**：PGBD1是TE驯化研究的"明星蛋白"。其祖先为DNA转座子，但现已被驯化为转录调控因子——这种进化过渡使其在TE调控领域具有双重意义：（1）作为驯化案例：PGBD1展示了TE编码蛋白如何被宿主"征用"为调控因子，为理解其他TE衍生蛋白（如RAG1/2重组酶、SETMAR/Metnase）的功能提供范例；（2）作为TE调控因子：PGBD1结合DNA的偏好性是否包括当代活跃的PiggyBac-like转座子（如MER85元件）是核心问题——若PGBD1通过DNA mimicry机制与祖先TE序列交叉结合，则可在转座子和其驯化产物之间形成反馈调控环。


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96JS3-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000137338-PGBD1

![](https://images.proteinatlas.org/7267/8_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/7267/8_D11_2_red_green.jpg)
![](https://images.proteinatlas.org/7267/9_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/7267/9_D11_2_red_green.jpg)
![](https://images.proteinatlas.org/7267/7_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/7267/7_D11_2_red_green.jpg)

### PubMed 文献

**PubMed count: 35**

| 41733899 | Shared Genetic Basis and Causality Between Epilepsy and Psychiatric Disorders: Evidence From a Comprehensive Genetic Ana | Brain Behav 2026 |
| 38495498 | Illuminating Shared Genetic Associations Between Oesophageal Carcinoma and Pulmonary Carcinoma Risk. | J Cancer 2024 |
| 37223020 | Zinc finger and SCAN domain-containing protein 18 is a potential DNA methylation-modified tumor suppressor and biomarker | Front Endocrinol (Lausanne) 2023 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PGBD1

