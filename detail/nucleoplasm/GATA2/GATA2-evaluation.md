---
type: protein-evaluation
gene: "GATA2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GATA2 — REJECTED (研究热度过高 (PubMed strict=1461，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GATA2 |
| 蛋白名称 | Endothelial transcription factor GATA-2 |
| 蛋白大小 | 480 aa / 50.5 kDa |
| UniProt ID | P23769 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 480 aa / 50.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1461 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.4; PDB: 5O9B, 6ZFV |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016374, IPR039355, IPR000679, IPR013088; Pfam:  |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **77.0/180** | |
| **归一化总分** | | | **42.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1461 |
| PubMed broad count | 2565 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The spectrum of GATA2 deficiency syndrome.. *Blood*. PMID: 36455197
2. GATA2 deficiency.. *Current opinion in allergy and clinical immunology*. PMID: 25397911
3. GATA2 links stemness to chemotherapy resistance in acute myeloid leukemia.. *Blood*. PMID: 39841459
4. GATA-related hematologic disorders.. *Experimental hematology*. PMID: 27235756
5. GATA2 and marrow failure.. *Best practice & research. Clinical haematology*. PMID: 34404529

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.4 |
| 高置信度残基 (pLDDT>90) 占比 | 16.2% |
| 置信残基 (pLDDT 70-90) 占比 | 4.2% |
| 中等置信 (pLDDT 50-70) 占比 | 22.9% |
| 低置信 (pLDDT<50) 占比 | 56.7% |
| 有序区域 (pLDDT>70) 占比 | 20.4% |
| 可用 PDB 条目 | 5O9B, 6ZFV |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=56.4），有序残基占 20.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016374, IPR039355, IPR000679, IPR013088; Pfam: PF00320 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SMAD4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15364|pubmed:21988832 |
| carB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Lmo2 | psi-mi:"MI:0096"(pull down) | pubmed:7568177|imex:IM-16983 |
| TAL1 | psi-mi:"MI:0018"(two hybrid) | pubmed:7568177|imex:IM-16983 |
| TCF3 | psi-mi:"MI:0018"(two hybrid) | pubmed:7568177|imex:IM-16983 |
| SNRPD3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| FHL3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| MDFI | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| PSMA3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TRIM23 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.4 + PDB: 5O9B, 6ZFV | pLDDT=56.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GATA2 — Endothelial transcription factor GATA-2，研究基础较多，新颖性有限。
2. 蛋白大小480 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1461 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=56.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1461 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P23769
- Protein Atlas: https://www.proteinatlas.org/ENSG00000179348-GATA2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GATA2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P23769
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000179348-GATA2/subcellular

![](https://images.proteinatlas.org/5633/59_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/5633/59_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/5633/60_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/5633/60_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/5633/61_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/5633/61_A9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
