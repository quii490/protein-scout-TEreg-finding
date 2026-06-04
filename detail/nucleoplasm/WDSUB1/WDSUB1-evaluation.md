---
type: protein-evaluation
gene: "WDSUB1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WDSUB1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WDSUB1 / WDSAM1 |
| 蛋白名称 | WD repeat, SAM and U-box domain-containing protein 1 |
| 蛋白大小 | 476 aa / 52.8 kDa |
| UniProt ID | Q8N9V3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Nucleoplasm, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 476 aa / 52.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001660, IPR013761, IPR003613, IPR052085, IPR015 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **137.5/180** | |
| **归一化总分** | | | **76.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: WDSAM1 |

**关键文献**:
1. Deafness-Associated ADGRV1 Mutation Impairs USH2A Stability through Improper Phosphorylation of WHRN and WDSUB1 Recruitment.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 37066759
2. [WDSUB1 knockdown alleviates dextran sulfate sodium-induced colitis in mice by inhibiting nuclear factor-κB signaling pathway].. *Nan fang yi ke da xue xue bao = Journal of Southern Medical University*. PMID: 36073209
3. Ancient origin of animal U-box ubiquitin ligases.. *BMC evolutionary biology*. PMID: 20979629

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.9 |
| 高置信度残基 (pLDDT>90) 占比 | 60.1% |
| 置信残基 (pLDDT 70-90) 占比 | 31.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.7% |
| 低置信 (pLDDT<50) 占比 | 2.9% |
| 有序区域 (pLDDT>70) 占比 | 91.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.9，有序区 91.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001660, IPR013761, IPR003613, IPR052085, IPR015943; Pfam: PF07647, PF04564, PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BAZ2B | 0.805 | 0.000 | — |
| TANC1 | 0.599 | 0.000 | — |
| WDR31 | 0.580 | 0.260 | — |
| BTBD2 | 0.538 | 0.000 | — |
| TTC37 | 0.516 | 0.406 | — |
| WDR86 | 0.473 | 0.000 | — |
| PDIK1L | 0.470 | 0.000 | — |
| ATG16L2 | 0.442 | 0.000 | — |
| UBE4A | 0.414 | 0.000 | — |
| SPO11 | 0.409 | 0.289 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 12，IntAct interactions: 0
- 调控相关比例: 1 / 12 = 8%

**评价**: STRING 12 个预测互作，IntAct 0 个实验互作。调控相关配体占比 8%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.9 + PDB: 无 | pLDDT=88.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli; 额外: Nucleoplasm, Cytosol | 待确认 |
| PPI | STRING + IntAct | 12 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. WDSUB1 — WD repeat, SAM and U-box domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小476 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N9V3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196151-WDSUB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WDSUB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N9V3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
