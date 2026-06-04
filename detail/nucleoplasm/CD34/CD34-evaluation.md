---
type: protein-evaluation
gene: "CD34"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CD34 — REJECTED (研究热度过高 (PubMed strict=11940，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CD34 |
| 蛋白名称 | Hematopoietic progenitor cell antigen CD34 |
| 蛋白大小 | 385 aa / 40.7 kDa |
| UniProt ID | P28906 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cell Junctions; 额外: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 385 aa / 40.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=11940 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008083, IPR013836; Pfam: PF06365 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cell Junctions; 额外: Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- apical plasma membrane (GO:0016324)
- basal plasma membrane (GO:0009925)
- cytoplasm (GO:0005737)
- external side of plasma membrane (GO:0009897)
- extracellular region (GO:0005576)
- glomerular endothelium fenestra (GO:0036053)
- intercellular bridge (GO:0045171)
- lysosome (GO:0005764)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11940 |
| PubMed broad count | 43999 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. CD34-Structure, Functions and Relationship with Cancer Stem Cells.. *Medicina (Kaunas, Lithuania)*. PMID: 37241170
2. Increased Anti-Inflammatory Therapeutic Potential and Progenitor Marker Expression of Corneal Mesenchymal Stem Cells Cultured in an Optimized Propagation Medium.. *Cell transplantation*. PMID: 38602231
3. CD34 protein is expressed in murine, canine, and porcine lungs.. *Canadian journal of veterinary research = Revue canadienne de recherche veterinaire*. PMID: 34248259
4. Endothelial CD34 expression and regulation of immune cell response in-vitro.. *Scientific reports*. PMID: 37598252
5. CRISPR/nCas9-Edited CD34+ Cells Rescue Mucopolysaccharidosis IVA Fibroblasts Phenotype.. *International journal of molecular sciences*. PMID: 40362571

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.4 |
| 高置信度残基 (pLDDT>90) 占比 | 27.0% |
| 置信残基 (pLDDT 70-90) 占比 | 7.0% |
| 中等置信 (pLDDT 50-70) 占比 | 16.9% |
| 低置信 (pLDDT<50) 占比 | 49.1% |
| 有序区域 (pLDDT>70) 占比 | 34.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=60.4），有序残基占 34.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008083, IPR013836; Pfam: PF06365 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SELL | 0.999 | 0.000 | — |
| CD38 | 0.964 | 0.000 | — |
| FN1 | 0.960 | 0.000 | — |
| KIT | 0.956 | 0.000 | — |
| SELE | 0.953 | 0.000 | — |
| CD33 | 0.951 | 0.000 | — |
| BCL2 | 0.945 | 0.000 | — |
| CSF3 | 0.940 | 0.000 | — |
| PECAM1 | 0.940 | 0.000 | — |
| KITLG | 0.934 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| A0A1S0QRP5 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| AGR2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.4 + PDB: 无 | pLDDT=60.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Plasma membrane, Cell Junctions; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CD34 — Hematopoietic progenitor cell antigen CD34，研究基础较多，新颖性有限。
2. 蛋白大小385 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11940 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 11940 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P28906
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174059-CD34/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CD34
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P28906
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
