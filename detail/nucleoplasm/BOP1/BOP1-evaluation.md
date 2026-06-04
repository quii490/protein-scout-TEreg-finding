---
type: protein-evaluation
gene: "BOP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BOP1 — REJECTED (研究热度过高 (PubMed strict=112，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BOP1 / KIAA0124 |
| 蛋白名称 | Ribosome biogenesis protein BOP1 |
| 蛋白大小 | 746 aa / 83.6 kDa |
| UniProt ID | Q14137 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoli, Nucleoli rim; 额外: Nucleoplasm, Mitotic chromosome; UniProt: Nucleus, nucleolus; Nucleus, nucleoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 746 aa / 83.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=112 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=79.7; PDB: 8FKP, 8FKQ, 8FKR, 8FKS, 8FKT, 8FKU, 8FKV |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028598, IPR012953, IPR015943, IPR019775, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **102.0/180** | |
| **归一化总分** | | | **56.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Nucleoli rim; 额外: Nucleoplasm, Mitotic chromosome | Enhanced |
| UniProt | Nucleus, nucleolus; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome (GO:0005694)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- PeBoW complex (GO:0070545)
- preribosome, large subunit precursor (GO:0030687)
- ribonucleoprotein complex (GO:1990904)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 112 |
| PubMed broad count | 148 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0124 |

**关键文献**:
1. Expression, Localization, and Function of the Nucleolar Protein BOP1 in Prostate Cancer Progression.. *The American journal of pathology*. PMID: 33039351
2. Bop1 is required to establish precursor domains of craniofacial tissues.. *Genesis (New York, N.Y. : 2000)*. PMID: 37974491
3. BOP1 Knockdown Attenuates Neointimal Hyperplasia by Activating p53 and Inhibiting Nascent Protein Synthesis.. *Oxidative medicine and cellular longevity*. PMID: 33510838
4. Functions of block of proliferation 1 during anterior development in Xenopus laevis.. *PloS one*. PMID: 36007075
5. BOP1 Used as a Novel Prognostic Marker and Correlated with Tumor Microenvironment in Pan-Cancer.. *Journal of oncology*. PMID: 34603446

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.7 |
| 高置信度残基 (pLDDT>90) 占比 | 48.5% |
| 置信残基 (pLDDT 70-90) 占比 | 30.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.2% |
| 低置信 (pLDDT<50) 占比 | 16.0% |
| 有序区域 (pLDDT>70) 占比 | 78.8% |
| 可用 PDB 条目 | 8FKP, 8FKQ, 8FKR, 8FKS, 8FKT, 8FKU, 8FKV, 8FKW, 8FKX, 8FKY |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（8FKP, 8FKQ, 8FKR, 8FKS, 8FKT, 8FKU, 8FKV, 8FKW, 8FKX, 8FKY）+ AlphaFold极高置信度预测（pLDDT=79.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028598, IPR012953, IPR015943, IPR019775, IPR036322; Pfam: PF08145, PF00400 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WDR12 | 0.999 | 0.992 | — |
| WDR74 | 0.999 | 0.969 | — |
| DDX18 | 0.999 | 0.965 | — |
| PES1 | 0.999 | 0.992 | — |
| NOC2L | 0.998 | 0.951 | — |
| GRWD1 | 0.998 | 0.088 | — |
| FTSJ3 | 0.998 | 0.940 | — |
| RSL1D1 | 0.998 | 0.943 | — |
| MRTO4 | 0.997 | 0.945 | — |
| GTPBP4 | 0.996 | 0.953 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ARRB1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ARRB2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PES1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16043514|imex:IM-20399 |
| WDR12 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16043514|imex:IM-20399 |
| WDR48 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| FLC1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CAND1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| RRP1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26310|pubmed:20926688 |
| RPS6 | psi-mi:"MI:0096"(pull down) | pubmed:29568061|imex:IM-26301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.7 + PDB: 8FKP, 8FKQ, 8FKR, 8FKS, 8FKT,  | pLDDT=79.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus; Nucleus, nucleoplasm / Nucleoli, Nucleoli rim; 额外: Nucleoplasm, Mitotic c | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. BOP1 — Ribosome biogenesis protein BOP1，研究基础较多，新颖性有限。
2. 蛋白大小746 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 112 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 112 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14137
- Protein Atlas: https://www.proteinatlas.org/ENSG00000261236-BOP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BOP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14137
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/BOP1/BOP1-PAE.png]]
