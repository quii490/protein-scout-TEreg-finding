---
type: protein-evaluation
gene: "RTF1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RTF1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RTF1 / KIAA0252 |
| 蛋白名称 | RNA polymerase-associated protein RTF1 homolog |
| 蛋白大小 | 710 aa / 80.3 kDa |
| UniProt ID | Q92541 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus, nucleoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 710 aa / 80.3 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=80 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.0; PDB: 2BZE, 2DB9, 3U1U, 4L1P, 4L1U, 6TED, 7UNC |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004343, IPR036128; Pfam: PF03126 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.0/180** | |
| **归一化总分** | | | **60.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Cdc73/Paf1 complex (GO:0016593)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 80 |
| PubMed broad count | 128 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0252 |

**关键文献**:
1. Rtf1-dependent transcriptional pausing regulates cardiogenesis.. *bioRxiv : the preprint server for biology*. PMID: 37873297
2. Rtf1 Transcriptionally Regulates Neonatal and Adult Cardiomyocyte Biology.. *Journal of cardiovascular development and disease*. PMID: 37233188
3. Rtf1-dependent transcriptional pausing regulates cardiogenesis.. *eLife*. PMID: 41537425
4. Rtf1 HMD domain facilitates global histone H2B monoubiquitination and regulates morphogenesis and virulence in the meningitis-causing pathogen Cryptococcus neoformans.. *eLife*. PMID: 40353352
5. A direct interaction between the Chd1 CHCT domain and Rtf1 controls Chd1 distribution and nucleosome positioning on active genes.. *Nucleic acids research*. PMID: 40867051

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.0 |
| 高置信度残基 (pLDDT>90) 占比 | 19.0% |
| 置信残基 (pLDDT 70-90) 占比 | 31.7% |
| 中等置信 (pLDDT 50-70) 占比 | 15.1% |
| 低置信 (pLDDT<50) 占比 | 34.2% |
| 有序区域 (pLDDT>70) 占比 | 50.7% |
| 可用 PDB 条目 | 2BZE, 2DB9, 3U1U, 4L1P, 4L1U, 6TED, 7UNC, 7UND, 8A3Y, 9EGX |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.0），有序残基占 50.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004343, IPR036128; Pfam: PF03126 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LEO1 | 0.999 | 0.997 | — |
| PAF1 | 0.999 | 0.997 | — |
| WDR61 | 0.999 | 0.854 | — |
| CDC73 | 0.999 | 0.995 | — |
| SUPT5H | 0.999 | 0.990 | — |
| CTR9 | 0.999 | 0.997 | — |
| SUPT4H1 | 0.998 | 0.948 | — |
| SUPT16H | 0.997 | 0.982 | — |
| POLR2A | 0.993 | 0.987 | — |
| SSRP1 | 0.992 | 0.963 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.0 + PDB: 2BZE, 2DB9, 3U1U, 4L1P, 4L1U,  | pLDDT=67.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. RTF1 — RNA polymerase-associated protein RTF1 homolog，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小710 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 80 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=67.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92541
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137815-RTF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RTF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92541
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
