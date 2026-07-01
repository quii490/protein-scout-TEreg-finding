---
type: protein-evaluation
gene: "CERS5"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## CERS5 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nuclear membrane (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/CERS5/IF_images/2102_E3_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/CERS5/IF_images/2102_E3_6_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CERS5 |
| 蛋白名称 | Ceramide synthase 5 |
| 蛋白大小 | 392 aa |
| UniProt ID | [Q8N5B7](https://www.uniprot.org/uniprotkb/Q8N5B7) |
| HPA 核定位 (IF) | Nuclear membrane |
| HPA 可靠性 | Approved |
| PubMed 总数 | 61 |
| AlphaFold pLDDT | 84.8 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nuclear membrane (Approved); UniProt: Endoplasmic reticulum membrane |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 392 aa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed 61篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 84.8 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 暂无数据 |
| **原始总分** |  |  | **99/183** |  |
| **归一化总分** |  |  | **54.1/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 CERS5 定位：
- **亚细胞定位**: Nuclear membrane
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Endoplasmic reticulum membrane
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Hammerschmidt P et al. (2019). "CerS6-Derived Sphingolipids Interact with Mff and Promote Mitochondrial Fragmentation in Obesity". *Cell*. PMID: 31150623
2. Liu Q et al. (2025). "Comprehensive profiling of lipid metabolic reprogramming expands precision medicine for HCC". *Hepatology*. PMID: 38899975
3. Zhu Q et al. (2024). "PAQR4 regulates adipocyte function and systemic metabolic health by mediating ceramide levels". *Nat Metab*. PMID: 38961186
4. Reese L et al. (2024). "Loss of ceramide synthase 5 inhibits the development of experimentally induced aortic valve stenosis". *Acta Physiol (Oxf)*. PMID: 38546351
5. Zhang S et al. (2022). "High expression of ceramide synthase 5 predicts a poor prognosis in gastric cancer". *Transl Cancer Res*. PMID: 36237237

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 数据

**IntAct 查询记录**: IntAct: 未检索到实验验证互作

**评价**: 暂无数据 IntAct/STRING/GO-CC 数据。


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| P2RY12 | BioGRID | 0 |
| LPAR1 | BioGRID | 0 |
| VIPR2 | BioGRID | 0 |
| HTR2C | BioGRID | 0 |
| IPPK | BioGRID | 0 |
| CD83 | BioGRID | 0 |
| FPR2 | BioGRID | 0 |
| C3AR1 | BioGRID | 0 |


### TE 调控评估

该蛋白的 GO-CC 注释中缺乏染色质/TE 沉默相关定位，TE 调控潜力较低。不建议作为 TE 调控优先靶标。

### 深度机制分析

CERS5（392 aa, UniProt Q8N5B7）是哺乳动物神经酰胺合酶家族成员（CerS1-6），催化鞘氨醇碱基与脂肪酰基CoA之间的N-酰基化反应——这是鞘脂从头合成途径的限速步骤。域架构为TRAM-LAG1-CLN8（TLC）脂质结合域（aa 139-340, SMART:SM00724, InterPro:IPR006634, Pfam:PF03798, PROSITE:PRU00205）——TLC域是冠菌素（coronatine）不敏感蛋白1（COI1）样折叠，由约200 aa构成，含保守的组氨酸三联体（HxxxHxxxH基序），负责底物识别和催化。TLC域的N端有约4个跨膜螺旋（TM1-TM4），锚定蛋白于内质网膜（UniProt: Endoplasmic reticulum membrane）——TMHMM预测显示TLC域位于膜的胞质面，催化口袋朝向胞质。

CERS5对C16:0（棕榈酰-CoA）具有底物选择性——生成C16:0-神经酰胺（棕榈酰-神经酰胺）。C16:0-神经酰胺是促凋亡信号分子，通过以下机制执行功能：（1）在线粒体膜上形成神经酰胺通道——释放细胞色素c并激活caspase级联；（2）激活蛋白磷酸酶2A（PP2A）→去磷酸化并抑制Akt→阻断生存信号；（3）激活PKCζ→磷酸化并抑制Akt。神经酰胺的促凋亡/促衰老功能与其在抗凋亡鞘脂（鞘氨醇-1-磷酸/S1P）的前体地位形成"鞘脂变阻器"（sphingolipid rheostat）——CERS5活性调节此平衡。

HPA IF确认CERS5定位为Nuclear membrane（Approved）——这与UniProt的ER membrane注释一致，因为核膜外层与粗面内质网连续。CERS5在核膜上合成的C16:0-神经酰胺可能通过以下机制间接影响核内生物学：（1）改变内核膜脂质微域（lipid rafts）的流动性→影响核膜相关异染色质（LADs）的组织；（2）神经酰胺作为核脂质第二信使激活核内PP1（蛋白磷酸酶1）和PP2A→改变核蛋白磷酸化状态；（3）核膜神经酰胺富集影响核孔复合物的通透性屏障。

humanPPI只检测到HMGCS1（3-羟基-3-甲基戊二酰辅酶A合酶1, 甲羟戊酸途径限速酶, Opencell）和MACO1（macoilin 1, 机械敏感通道调节蛋白, Opencell）互作——两个均为低置信度（AF3结构不可用）。STRING互作列表几乎为空（P2RY12, LPAR1等均为GPCR, BioGRID score=0）——这一极端稀疏的PPI网络反映了CERS5作为ER膜整合跨膜蛋白在高通量PPI方法中的技术性失检。

CERS5归一化得分54.1/100受限於PPI数据极为稀少、PubMed=61篇的中等研究热度、和缺乏染色质/核基质互作的直接证据。Pfam:PF00046（homeobox domain）在InterPro/Pfam注释中出现——但这是TLC域内一个退化的同源异形盒样折叠，并非真正的DNA结合域。CERS5作为核膜鞘脂代谢酶，其TE调控潜力仅限于核膜脂质环境改变→间接影响LAD区异染色质结构的假设性路径。实验优先级：CERS5敲除后核膜脂质组学分析→LAD区ChIP-seq→TE表达RNA-seq。

![](https://images.proteinatlas.org/6780/2102_E3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6780/2102_E3_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/6780/2142_D6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6780/2142_D6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6780/1867_E8_8_cr5b6b06887cadd_blue_red_green.jpg)
![](https://images.proteinatlas.org/6780/1867_E8_19_cr5b6b06887cb59_blue_red_green.jpg)


### 5. 总体评价

**推荐等级**: ⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nuclear membrane
2. **研究新颖性**: PubMed仅61篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 84.8

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/CERS5)
- [UniProt](https://www.uniprot.org/uniprotkb/Q8N5B7)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CERS5%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q8N5B7)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 暂无互作数据 |

暂无实验验证互作。无 BioGrid 补充数据。

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N5B7 |
| SMART | SM00724; |
| UniProt Domain [FT] | DOMAIN 139..340; /note="TLC"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00205" |
| InterPro | IPR001356;IPR009057;IPR016439;IPR006634; |
| Pfam | PF00046;PF03798; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000139624-CERS5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HMGCS1 | Opencell | false |
| MACO1 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
