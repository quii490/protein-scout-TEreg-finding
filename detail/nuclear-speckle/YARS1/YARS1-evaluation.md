---
type: protein-evaluation
gene: "YARS1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## YARS1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | YARS1 / YARS |
| 蛋白名称 | Tyrosine--tRNA ligase, cytoplasmic |
| 蛋白大小 | 528 aa / 59.1 kDa |
| UniProt ID | P54577 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nuclear bodies; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 528 aa / 59.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=24 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=90.8; PDB: 1N3L, 1NTG, 1Q11, 4Q93, 4QBT, 5THH, 5THL |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002305, IPR012340, IPR014729, IPR002547, IPR002 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.0/180** | |
| **归一化总分** | | | **75.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nuclear bodies | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular space (GO:0005615)
- nuclear body (GO:0016604)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 32 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: YARS |

**关键文献**:
1. Charcot-Marie-Tooth Hereditary Neuropathy Overview.. **. PMID: 20301532
2. YARS1 Deficiency.. **. PMID: 40608960
3. The recurrent missense mutation p.(Arg367Trp) in YARS1 causes a distinct neurodevelopmental phenotype.. *Journal of molecular medicine (Berlin, Germany)*. PMID: 34536092
4. Drosophila Models for Charcot-Marie-Tooth Neuropathy Related to Aminoacyl-tRNA Synthetases.. *Genes*. PMID: 34680913
5. Tyrosine and Phenylalanine Activate Neuronal DNA Repair but Exhibit Opposing Effects on Global Transcription and Adult Female Mice Are Resilient to TyrRS/YARS1 Depletion.. *IUBMB life*. PMID: 40476370

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.8 |
| 高置信度残基 (pLDDT>90) 占比 | 78.2% |
| 置信残基 (pLDDT 70-90) 占比 | 14.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.0% |
| 低置信 (pLDDT<50) 占比 | 3.0% |
| 有序区域 (pLDDT>70) 占比 | 93.0% |
| 可用 PDB 条目 | 1N3L, 1NTG, 1Q11, 4Q93, 4QBT, 5THH, 5THL, 7ROU |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1N3L, 1NTG, 1Q11, 4Q93, 4QBT, 5THH, 5THL, 7ROU）+ AlphaFold极高置信度预测（pLDDT=90.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002305, IPR012340, IPR014729, IPR002547, IPR002307; Pfam: PF00579, PF01588 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EPRS1 | 0.999 | 0.853 | — |
| MARS1 | 0.999 | 0.967 | — |
| WARS1 | 0.997 | 0.071 | — |
| AARS1 | 0.996 | 0.067 | — |
| WARS2 | 0.991 | 0.062 | — |
| GARS1 | 0.989 | 0.000 | — |
| KARS1 | 0.988 | 0.314 | — |
| LARS1 | 0.980 | 0.484 | — |
| LARS2 | 0.979 | 0.484 | — |
| MARS2 | 0.975 | 0.095 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FTSJ1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GABARAPL2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EIF1B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SAP18 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TRAF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EIF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ARF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| DLD | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.8 + PDB: 1N3L, 1NTG, 1Q11, 4Q93, 4QBT,  | pLDDT=90.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. YARS1 — Tyrosine--tRNA ligase, cytoplasmic，非常新颖，仅有少数基础研究。
2. 蛋白大小528 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 24 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P54577
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134684-YARS1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=YARS1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P54577
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
