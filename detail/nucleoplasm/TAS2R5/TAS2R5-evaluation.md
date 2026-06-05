---
type: protein-evaluation
gene: "TAS2R5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TAS2R5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TAS2R5 |
| 蛋白名称 | Taste receptor type 2 member 5 |
| 蛋白大小 | 299 aa / 34.5 kDa |
| UniProt ID | Q9NYW4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Nucleoli; 额外: Cytoplasmic bodies; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 299 aa / 34.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR007960; Pfam: PF05296 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli; 额外: Cytoplasmic bodies | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 38 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Agonist activation to open the Gα subunit of the GPCR-G protein precoupled complex defines functional agonist activation of TAS2R5.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 39565310
2. Polymorphism of TAS2R3, TAS2R5, TAS2R19, and TAS2R50 genes and bitter food intake frequency inelderly woman.. *Acta scientiarum polonorum. Technologia alimentaria*. PMID: 32227702
3. The repertoire of bitter taste receptor genes in canids.. *Amino acids*. PMID: 28417226
4. TAS2R5 screening reveals biased agonism that fails to evoke internalization and downregulation resulting in attenuated desensitization.. *PloS one*. PMID: 39946435
5. Dynamic Pathway Selectivity of TAS2R5 toward or Away from β-Arrestin or G Protein from Biased Agonists.. *Biochemistry*. PMID: 42142023

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.2 |
| 高置信度残基 (pLDDT>90) 占比 | 23.1% |
| 置信残基 (pLDDT 70-90) 占比 | 58.2% |
| 中等置信 (pLDDT 50-70) 占比 | 17.7% |
| 低置信 (pLDDT<50) 占比 | 1.0% |
| 有序区域 (pLDDT>70) 占比 | 81.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=80.2，有序区 81.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007960; Pfam: PF05296 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RTP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMEM187 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SLC30A2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SFT2D2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| VAMP5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CCL4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 6
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.2 + PDB: 无 | pLDDT=80.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm, Nucleoli; 额外: Cytoplasmic bodies | 一致 |
| PPI | STRING + IntAct | 0 + 6 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TAS2R5 — Taste receptor type 2 member 5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小299 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NYW4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000127366-TAS2R5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TAS2R5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NYW4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000127366-TAS2R5/subcellular

![](https://images.proteinatlas.org/53742/1692_D4_23_cr57d296716da6b_red_green.jpg)
![](https://images.proteinatlas.org/53742/1692_D4_3_cr57d29669c08c4_red_green.jpg)
![](https://images.proteinatlas.org/53742/1791_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/53742/1791_E3_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NYW4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
