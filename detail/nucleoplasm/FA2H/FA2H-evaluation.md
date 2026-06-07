---
type: protein-evaluation
gene: "FA2H"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FA2H — REJECTED (研究热度过高 (PubMed strict=129，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FA2H / FAAH, FAXDC1 |
| 蛋白名称 | Fatty acid 2-hydroxylase |
| 蛋白大小 | 372 aa / 42.8 kDa |
| UniProt ID | Q7L5A8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear membrane; UniProt: Endoplasmic reticulum membrane; Microsome membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 372 aa / 42.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=129 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001199, IPR036400, IPR018506, IPR006694, IPR014 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.5/180** | |
| **归一化总分** | | | **42.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane | Uncertain |
| UniProt | Endoplasmic reticulum membrane; Microsome membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 129 |
| PubMed broad count | 191 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAAH, FAXDC1 |

**关键文献**:
1. Neurodegeneration with brain iron accumulation.. *Handbook of clinical neurology*. PMID: 29325618
2. Hereditary spastic paraplegia: clinico-pathologic features and emerging molecular mechanisms.. *Acta neuropathologica*. PMID: 23897027
3. Long-chain sulfatide enrichment is an actionable metabolic vulnerability in intraductal papillary mucinous neoplasm (IPMN)-associated pancreatic cancers.. *Gut*. PMID: 40268349
4. Neurodegeneration with Brain Iron Accumulation.. *Advances in experimental medicine and biology*. PMID: 40603798
5. Dysregulated ceramides metabolism by fatty acid 2-hydroxylase exposes a metabolic vulnerability to target cancer metastasis.. *Signal transduction and targeted therapy*. PMID: 36274060

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.1 |
| 高置信度残基 (pLDDT>90) 占比 | 65.6% |
| 置信残基 (pLDDT 70-90) 占比 | 20.4% |
| 中等置信 (pLDDT 50-70) 占比 | 3.2% |
| 低置信 (pLDDT<50) 占比 | 10.8% |
| 有序区域 (pLDDT>70) 占比 | 86.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.1，有序区 86.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001199, IPR036400, IPR018506, IPR006694, IPR014430; Pfam: PF00173, PF04116 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AGMO | 0.943 | 0.000 | — |
| C19orf12 | 0.853 | 0.000 | — |
| FAXDC2 | 0.799 | 0.166 | — |
| ALDH3A2 | 0.782 | 0.063 | — |
| MSMO1 | 0.776 | 0.166 | — |
| PANK2 | 0.736 | 0.000 | — |
| DCAF17 | 0.718 | 0.000 | — |
| COASY | 0.717 | 0.000 | — |
| CH25H | 0.703 | 0.166 | — |
| UGT8 | 0.694 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UBQLN4 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| CREB3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| ERLIN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MSR1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PEX12 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SYT2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TMEM41A | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SLC10A1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| AQP6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ELOVL4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.1 + PDB: 无 | pLDDT=85.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Microsome membrane / Nuclear membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FA2H — Fatty acid 2-hydroxylase，研究基础较多，新颖性有限。
2. 蛋白大小372 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 129 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 129 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7L5A8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000103089-FA2H/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FA2H
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7L5A8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (uncertain)。来源: https://www.proteinatlas.org/ENSG00000103089-FA2H/subcellular

![](https://images.proteinatlas.org/77840/1702_F8_32_blue_red_green.jpg)
![](https://images.proteinatlas.org/77840/1702_F8_35_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7L5A8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7L5A8 |
| SMART | SM01117; |
| UniProt Domain [FT] | DOMAIN 8..86; /note="Cytochrome b5 heme-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00279"; DOMAIN 219..361; /note="Fatty acid hydroxylase"; /evidence="ECO:0000255" |
| InterPro | IPR001199;IPR036400;IPR018506;IPR006694;IPR014430; |
| Pfam | PF00173;PF04116; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000103089-FA2H/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AQP6 | Intact | false |
| ATP1A3 | Bioplex | false |
| CD79A | Intact | false |
| CREB3L1 | Intact | false |
| DDX20 | Bioplex | false |
| DLG2 | Intact | false |
| DYNC1H1 | Intact | false |
| EBP | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
