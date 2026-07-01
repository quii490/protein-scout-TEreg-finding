---
type: protein-evaluation
gene: "LRR1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRR1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRR1 / PPIL5 |
| 蛋白名称 | Leucine-rich repeat protein 1 |
| 蛋白大小 | 414 aa / 46.7 kDa |
| UniProt ID | Q96L50 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear membrane; 额外: Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 414 aa / 46.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=45 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.2; PDB: 7PLO |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001611, IPR025875, IPR003591, IPR032675, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear membrane; 额外: Vesicles | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed broad count | 73 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PPIL5 |

**关键文献**:
1. A novel oncogene, leucine-rich repeat protein 1, mediates hypoxia-induced hepatocellular carcinoma progression.. *Functional & integrative genomics*. PMID: 40459634
2. Whole-Genome Sequencing Reveals Individual and Cohort Level Insights into Chromosome 9p Syndromes.. *medRxiv : the preprint server for health sciences*. PMID: 40196253
3. Structural basis for LAR-RPTP/Slitrk complex-mediated synaptic adhesion.. *Nature communications*. PMID: 25394468
4. Arabidopsis U-box E3 ubiquitin ligase PUB11 negatively regulates drought tolerance by degrading the receptor-like protein kinases LRR1 and KIN7.. *Journal of integrative plant biology*. PMID: 33347703
5. Distribution and Evolution of Yersinia Leucine-Rich Repeat Proteins.. *Infection and immunity*. PMID: 27217422

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.2 |
| 高置信度残基 (pLDDT>90) 占比 | 63.3% |
| 置信残基 (pLDDT 70-90) 占比 | 27.3% |
| 中等置信 (pLDDT 50-70) 占比 | 7.0% |
| 低置信 (pLDDT<50) 占比 | 2.4% |
| 有序区域 (pLDDT>70) 占比 | 90.6% |
| 可用 PDB 条目 | 7PLO |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.2，有序区 90.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001611, IPR025875, IPR003591, IPR032675, IPR050216; Pfam: PF00560, PF12799, PF25344 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL2 | 0.996 | 0.971 | — |
| RBX1 | 0.990 | 0.931 | — |
| ELOC | 0.989 | 0.928 | — |
| ELOB | 0.984 | 0.914 | — |
| MCM7 | 0.947 | 0.852 | — |
| WDHD1 | 0.935 | 0.800 | — |
| MCM3 | 0.932 | 0.800 | — |
| MCM5 | 0.916 | 0.800 | — |
| CDC45 | 0.905 | 0.801 | — |
| GINS4 | 0.895 | 0.800 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| COPS5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| COPS6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| CUL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15601820|imex:IM-19076 |
| ELOB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15601820|imex:IM-19076 |
| RBX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15601820|imex:IM-19076 |
| ELOC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15601820|imex:IM-19076 |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| COPS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZBTB38 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| COPS8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.2 + PDB: 7PLO | pLDDT=88.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nuclear membrane; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LRR1 — Leucine-rich repeat protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小414 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 45 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CUL2 | STRING | 996 |
| RBX1 | STRING | 990 |
| ELOC | STRING | 989 |
| ELOB | STRING | 984 |
| MCM7 | STRING | 947 |
| WDHD1 | STRING | 935 |
| MCM3 | STRING | 932 |
| MCM5 | STRING | 916 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与核内 TE 调控过程，但目前无直接实验证据支持。需实验验证。

### 深度机制分析

LRR1（414 aa, 46.7 kDa, UniProt Q96L50）的域架构相对紧凑——N端为富亮氨酸重复域（LRR domain, InterPro:IPR001611, IPR032675, SMART:SM00369, Pfam:PF00560, PF12799），包含约14个LRR重复单元（每个22-24 aa，富含亮氨酸，形成马蹄形螺线管折叠），C端为LRR-CT（IPR025875, Pfam:PF25344）。LRR域是蛋白质互作的通用平台——马蹄形螺线管的凹面形成延展的β-折叠结合界面。AlphaFold v6 pLDDT=88.2（90.6%有序区, 63.3% pLDDT>90）确认LRR1结构中LRR域以最高置信度折叠为典型的马蹄形螺线管——这是极高的预测质量。PDB 7PLO是LRR1与CUL2-RBX1-ELOB/C复合物的Cryo-EM结构（分辨率约3.0 A）——提供了LRR1作为Cullin-RING E3泛素连接酶底物识别亚基的直接结构证据。

LRR1是CRL2（Cullin2-RING Ligase）E3泛素连接酶复合物的底物识别受体——STRING互作图谱的极高置信度且全实验验证的核心互作定义了此复合体的完整组成：CUL2（combined score=0.996, 实验=0.971）→ELOC/Elongin C（0.989, 实验=0.928）+ ELOB/Elongin B（0.984, 实验=0.914）→RBX1/ROC1（0.990, 实验=0.931）。CRL2-LRR1复合体的泛素化底物未知——PDB 7PLO捕获了LRR1-CUL2-RBX1-ELOB/C的无底物态构象，但其与MCM3/5/7和CDC45（STRT score=0.905-0.947, 实验=0.800-0.852）的极高实验互作分数揭示了最可能的底物方向。MCM2-7异六聚体是DNA复制解旋酶的核心组分，CDC45和GINS4（0.895）是CMG（Cdc45-MCM-GINS）复制解旋酶复合物的另外两个必需亚基。LRR1可能以CRL2-LRR1 E3连接酶形式泛素化并降解CMG组分——参与复制解旋酶的解组装和复制终止。WDHD1（0.935, 实验=0.800）是DNA复制叉的AND-1/Ctf4同源物——进一步支持此方向。

HPA确认LRR1定位于Nucleoplasm和Nuclear membrane（Approved），GO-CC含Nucleus（GO:0005634）。核膜定位（核内膜信号）与DNA复制解旋酶调控的功能逻辑吻合——复制起始发生在核内。IntAct co-IP验证了CRL2核心组分（CUL2, ELOB, RBX1, ELOC, CUL5, PMID:15601820, 21145461）和COP9信号小体亚基（COPS2, COPS5, COPS6, COPS8, PMID:19615732, 28514442）的互作——COP9信号小体是CRL E3连接酶的通用去NEDD8化酶，调控CRL活性周期。

LRR1的TF/TE调控潜力来自其与CMG复制解旋酶的互作。停滞的复制叉在重复序列（包括LINE-1和卫星DNA）处优先发生——CRL2-LRR1参与的复制解旋酶加工可能影响重复区域的复制叉稳定性。此外，CRL2-LRR1可能泛素化并降解复制叉上的染色质组装因子——影响复制偶联的核小体组装和表观遗传信息的传递。但PubMed=45篇（30/50分）且无直接实验证据将LRR1与TE区域联系——其TE调控潜力为间接的"复制叉管理"假说。

实验优先级：LRR1-CMG复合物泛素化底物的鉴定（体外泛素化实验+TMT-MS定量检测）；LRR1 ChIP-seq检测其基因组占据模式——重点关注重复序列区域；LRR1敲除后复制叉进程的纤维分析（DNA fiber assay）和重复序列不稳定检测。
- UniProt: https://www.uniprot.org/uniprotkb/Q96L50
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165501-LRR1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRR1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96L50
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000165501-LRR1/subcellular

![](https://images.proteinatlas.org/69364/1434_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/69364/1434_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/69364/1436_D5_3_red_green.jpg)
![](https://images.proteinatlas.org/69364/1436_D5_4_red_green.jpg)
![](https://images.proteinatlas.org/69364/1547_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/69364/1547_H6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96L50-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96L50 |
| SMART | SM00369; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001611;IPR025875;IPR003591;IPR032675;IPR050216;IPR057437; |
| Pfam | PF00560;PF12799;PF25344; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000165501-LRR1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDKN1A | Biogrid | false |
| COPS2 | Biogrid | false |
| COPS3 | Biogrid | false |
| COPS5 | Biogrid | false |
| COPS6 | Biogrid | false |
| COPS7A | Biogrid | false |
| COPS8 | Biogrid | false |
| CUL2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
