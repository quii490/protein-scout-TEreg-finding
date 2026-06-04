---
type: protein-evaluation
gene: "DSCC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DSCC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DSCC1 / DCC1 |
| 蛋白名称 | Sister chromatid cohesion protein DCC1 |
| 蛋白大小 | 393 aa / 44.8 kDa |
| UniProt ID | Q9BVC3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 393 aa / 44.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR019128; Pfam: PF09724 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.0/180** | |
| **归一化总分** | | | **75.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromosome, centromeric region (GO:0000775)
- Ctf18 RFC-like complex (GO:0031390)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 36 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DCC1 |

**关键文献**:
1. Genetic determinants of micronucleus formation in vivo.. *Nature*. PMID: 38355793
2. Roles of DSCC1 and GINS1 in gastric cancer.. *Medicine*. PMID: 37904396
3. ADAMTSL2 is an independent predictor for the prognosis of gastric cancer.. *Discover oncology*. PMID: 40252157
4. Characterization of the prognostic, diagnostic, and immunological roles of DSCC1 and its genomic alteration and instability in human cancers.. *Cellular and molecular biology (Noisy-le-Grand, France)*. PMID: 38678604
5. Complementary biomarkers of computed tomography for diagnostic grading of gastric cancer: DSCC1 and GINS1.. *Aging*. PMID: 38301047

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.6 |
| 高置信度残基 (pLDDT>90) 占比 | 75.6% |
| 置信残基 (pLDDT 70-90) 占比 | 20.1% |
| 中等置信 (pLDDT 50-70) 占比 | 4.1% |
| 低置信 (pLDDT<50) 占比 | 0.3% |
| 有序区域 (pLDDT>70) 占比 | 95.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.6，有序区 95.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019128; Pfam: PF09724 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RFC2 | 0.999 | 0.816 | — |
| CHTF8 | 0.999 | 0.987 | — |
| RFC5 | 0.999 | 0.820 | — |
| CHTF18 | 0.999 | 0.990 | — |
| RFC3 | 0.999 | 0.845 | — |
| RFC4 | 0.998 | 0.776 | — |
| POLE | 0.943 | 0.893 | — |
| SMC3 | 0.905 | 0.127 | — |
| ESCO2 | 0.903 | 0.117 | — |
| ESCO1 | 0.889 | 0.117 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.6 + PDB: 无 | pLDDT=91.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DSCC1 — Sister chromatid cohesion protein DCC1，非常新颖，仅有少数基础研究。
2. 蛋白大小393 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BVC3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136982-DSCC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DSCC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BVC3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DSCC1/IF_images/DSCC1_A_431_1.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DSCC1/IF_images/DSCC1_A_431_2.jpg]]
