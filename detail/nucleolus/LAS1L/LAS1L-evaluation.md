---
type: protein-evaluation
gene: "LAS1L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LAS1L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LAS1L |
| 蛋白名称 | Ribosomal biogenesis protein LAS1L |
| 蛋白大小 | 734 aa / 83.1 kDa |
| UniProt ID | Q9Y4W2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Primary cilium transition zone, Centriolar ; UniProt: Nucleus, nucleolus; Nucleus, nucleoplasm; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 734 aa / 83.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.5; PDB: 8FL2, 8FL3, 8FL4, 9DUN |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007174; Pfam: PF04031 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Primary cilium transition zone, Centriolar satellite, Centrosome, Basal body, Cytosol | Approved |
| UniProt | Nucleus, nucleolus; Nucleus, nucleoplasm; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Las1 complex (GO:0090730)
- membrane (GO:0016020)
- MLL1 complex (GO:0071339)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 28 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. X-exome sequencing of 405 unresolved families identifies seven novel intellectual disability genes.. *Molecular psychiatry*. PMID: 25644381
2. Molecular insights into the overall architecture of human rixosome.. *Nature communications*. PMID: 40195365
3. New genes involved in Angelman syndrome-like: Expanding the genetic spectrum.. *PloS one*. PMID: 34653234
4. Las1L is a nucleolar protein required for cell proliferation and ribosome biogenesis.. *Molecular and cellular biology*. PMID: 20647540
5. Inhibiting β-catenin disables nucleolar functions in triple-negative breast cancer.. *Cell death & disease*. PMID: 33664239

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.5 |
| 高置信度残基 (pLDDT>90) 占比 | 23.6% |
| 置信残基 (pLDDT 70-90) 占比 | 23.4% |
| 中等置信 (pLDDT 50-70) 占比 | 12.3% |
| 低置信 (pLDDT<50) 占比 | 40.7% |
| 有序区域 (pLDDT>70) 占比 | 47.0% |
| 可用 PDB 条目 | 8FL2, 8FL3, 8FL4, 9DUN |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=62.5），有序残基占 47.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007174; Pfam: PF04031 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NOL9 | 0.999 | 0.998 | — |
| PELP1 | 0.998 | 0.880 | — |
| TEX10 | 0.998 | 0.815 | — |
| SENP3 | 0.996 | 0.777 | — |
| WDR18 | 0.991 | 0.854 | — |
| WDR5 | 0.940 | 0.177 | — |
| TAF1 | 0.928 | 0.095 | — |
| MCRS1 | 0.920 | 0.000 | — |
| CHD8 | 0.914 | 0.000 | — |
| KMT2A | 0.912 | 0.096 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PNKP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TSC22D1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MYC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ESR2 | psi-mi:"MI:0029"(cosedimentation through density g | imex:IM-13781|pubmed:21182203 |
| ETS1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| FOS | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CAND1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| RRP1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26310|pubmed:20926688 |
| CDK8 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.5 + PDB: 8FL2, 8FL3, 8FL4, 9DUN | pLDDT=62.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus; Nucleus, nucleoplasm; Cytoplas / Nucleoplasm; 额外: Primary cilium transition zone, C | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LAS1L — Ribosomal biogenesis protein LAS1L，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小734 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=62.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y4W2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000001497-LAS1L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LAS1L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y4W2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
