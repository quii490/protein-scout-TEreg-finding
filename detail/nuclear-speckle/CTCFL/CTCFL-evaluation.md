---
type: protein-evaluation
gene: "CTCFL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CTCFL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CTCFL / BORIS |
| 蛋白名称 | Transcriptional repressor CTCFL |
| 蛋白大小 | 663 aa / 75.7 kDa |
| UniProt ID | Q8NI51 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 663 aa / 75.7 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=86 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036236, IPR013087; Pfam: PF00096 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **90.0/180** | |
| **归一化总分** | | | **50.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies; 额外: Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome (GO:0005694)
- cytosol (GO:0005829)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 86 |
| PubMed broad count | 176 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BORIS |

**关键文献**:
1. CTCF and CTCFL in cancer.. *Current opinion in genetics & development*. PMID: 32334335
2. Interaction of CTCF and CTCFL in genome regulation through chromatin architecture during the spermatogenesis and carcinogenesis.. *PeerJ*. PMID: 39430552
3. BORIS/CTCFL epigenetically reprograms clustered CTCF binding sites into alternative transcriptional start sites.. *Genome biology*. PMID: 38297316
4. PRAME and CTCFL-reactive TCRs for the treatment of ovarian cancer.. *Frontiers in immunology*. PMID: 37026005
5. Defining the relative and combined contribution of CTCF and CTCFL to genomic regulation.. *Genome biology*. PMID: 32393311

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.9 |
| 高置信度残基 (pLDDT>90) 占比 | 14.5% |
| 置信残基 (pLDDT 70-90) 占比 | 31.5% |
| 中等置信 (pLDDT 50-70) 占比 | 3.6% |
| 低置信 (pLDDT<50) 占比 | 50.4% |
| 有序区域 (pLDDT>70) 占比 | 46.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=54.9），有序残基占 46.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036236, IPR013087; Pfam: PF00096 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRMT7 | 0.897 | 0.310 | — |
| RAD21 | 0.887 | 0.463 | — |
| STAG2 | 0.840 | 0.602 | — |
| SMC3 | 0.758 | 0.066 | — |
| NIPBL | 0.707 | 0.000 | — |
| EZH2 | 0.706 | 0.211 | — |
| CHD8 | 0.702 | 0.102 | — |
| IGF2 | 0.664 | 0.000 | — |
| STAG1 | 0.655 | 0.439 | — |
| RAD21L1 | 0.653 | 0.463 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CTCF | psi-mi:"MI:0096"(pull down) | pubmed:10734189|imex:IM-19405 |
| Sin3a | psi-mi:"MI:0096"(pull down) | pubmed:10734189|imex:IM-19405 |
| YBX1 | psi-mi:"MI:0096"(pull down) | pubmed:15229244|imex:IM-19626 |
| Chd8 | psi-mi:"MI:0096"(pull down) | pubmed:16949368|imex:IM-19012 |
| Taf3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21884934|imex:IM-16573 |
| CAND1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| H3C1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| FBL | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| RPS6 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| DNAJC21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.9 + PDB: 无 | pLDDT=54.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Nuclear bodies; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. CTCFL — Transcriptional repressor CTCFL，研究基础较多，新颖性有限。
2. 蛋白大小663 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 86 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=54.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NI51
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124092-CTCFL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CTCFL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NI51
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
