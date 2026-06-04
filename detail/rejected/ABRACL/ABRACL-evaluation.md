---
type: protein-evaluation
gene: "ABRACL"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ABRACL — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ABRACL / C6orf115 |
| 蛋白名称 | Costars family protein ABRACL |
| 蛋白大小 | 81 aa / 9.1 kDa |
| UniProt ID | Q9P1F3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 81 aa / 9.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=94.8; PDB: 2L2O |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR044302, IPR027817, IPR038095; Pfam: PF14705 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 8 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.5/180** | |
| **归一化总分** | | | **65.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C6orf115 |

**关键文献**:
1. Identification of biomarker associated with Trop2 in breast cancer: implication for targeted therapy.. *Discover oncology*. PMID: 39240479
2. Human Costars Family Protein ABRACL Modulates Actin Dynamics and Cell Migration and Associates with Tumorigenic Growth.. *International journal of molecular sciences*. PMID: 33670794
3. Stemness-Relevant Gene Signature for Chemotherapeutic Response and Prognosis Prediction in Ovarian Cancer.. *Stem cells international*. PMID: 40182754
4. Characterization of the Abracl-Expressing Cell Populations in the Embryonic Mammalian Telencephalon.. *Biomolecules*. PMID: 37759737
5. ABRACL upregulated by transcription factor CBX4 promotes proliferation and migration and inhibits the apoptosis of gastric cancer cells.. *Histology and histopathology*. PMID: 39376051

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.8 |
| 高置信度残基 (pLDDT>90) 占比 | 90.1% |
| 置信残基 (pLDDT 70-90) 占比 | 8.6% |
| 中等置信 (pLDDT 50-70) 占比 | 1.2% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 98.7% |
| 可用 PDB 条目 | 2L2O |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.8，有序区 98.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR044302, IPR027817, IPR038095; Pfam: PF14705 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMIM18 | 0.554 | 0.000 | — |
| TTC9B | 0.504 | 0.000 | — |
| IRGQ | 0.494 | 0.000 | — |
| CXorf38 | 0.448 | 0.000 | — |
| DMAC2 | 0.439 | 0.000 | — |
| LRFN3 | 0.435 | 0.000 | — |
| SBK1 | 0.429 | 0.000 | — |
| MEF2C | 0.415 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DCTN1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| SASS6 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| CNTRL | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| RPGRIP1L | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 8，IntAct interactions: 4
- 调控相关比例: 0 / 8 = 0%

**评价**: STRING 8 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.8 + PDB: 2L2O | pLDDT=94.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 8 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ABRACL — Costars family protein ABRACL，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小81 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P1F3
- Protein Atlas: https://www.proteinatlas.org/search/ABRACL
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ABRACL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P1F3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/ABRACL/ABRACL-PAE.png]]
