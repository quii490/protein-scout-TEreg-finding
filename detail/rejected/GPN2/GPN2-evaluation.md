---
type: protein-evaluation
gene: "GPN2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPN2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPN2 / ATPBD1B |
| 蛋白名称 | GPN-loop GTPase 2 |
| 蛋白大小 | 310 aa / 34.6 kDa |
| UniProt ID | Q9H9Y4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 310 aa / 34.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR004130, IPR030231, IPR027417; Pfam: PF03029 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.0/180** | |
| **归一化总分** | | | **63.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ATPBD1B |

**关键文献**:
1. Rba50 and Gpn2 recruit the second largest subunits for the assembly of RNA polymerase II and III.. *International journal of biological macromolecules*. PMID: 35176321
2. Biogenesis of RNA polymerases II and III requires the conserved GPN small GTPases in Saccharomyces cerevisiae.. *Genetics*. PMID: 23267056
3. A nuclear proteome localization screen reveals the exquisite specificity of Gpn2 in RNA polymerase biogenesis.. *Cell cycle (Georgetown, Tex.)*. PMID: 34180355
4. Dosage suppressors of gpn2ts mutants and functional insights into the role of Gpn2 in budding yeast.. *PloS one*. PMID: 39642114
5. Npa3 interacts with Gpn3 and assembly factor Rba50 for RNA polymerase II biogenesis.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 32985767

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.4 |
| 高置信度残基 (pLDDT>90) 占比 | 55.5% |
| 置信残基 (pLDDT 70-90) 占比 | 28.7% |
| 中等置信 (pLDDT 50-70) 占比 | 8.4% |
| 低置信 (pLDDT<50) 占比 | 7.4% |
| 有序区域 (pLDDT>70) 占比 | 84.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=84.4，有序区 84.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004130, IPR030231, IPR027417; Pfam: PF03029 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GPN1 | 0.982 | 0.964 | — |
| RPAP1 | 0.958 | 0.846 | — |
| POLR2B | 0.941 | 0.841 | — |
| POLR2J | 0.928 | 0.840 | — |
| POLR2L | 0.913 | 0.775 | — |
| POLR2C | 0.906 | 0.753 | — |
| POLR2M | 0.841 | 0.797 | — |
| POLR2K | 0.729 | 0.258 | — |
| GPN3 | 0.709 | 0.187 | — |
| POLR2J3 | 0.704 | 0.632 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ADH1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| FAS1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| HEF3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| PDC1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| PSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPP0 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| URA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.4 + PDB: 无 | pLDDT=84.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GPN2 — GPN-loop GTPase 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小310 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H9Y4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000142751-GPN2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPN2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H9Y4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
