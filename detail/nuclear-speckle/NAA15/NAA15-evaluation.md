---
type: protein-evaluation
gene: "NAA15"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NAA15 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NAA15 / GA19, NARG1, NATH, TBDN100 |
| 蛋白名称 | N-alpha-acetyltransferase 15, NatA auxiliary subunit |
| 蛋白大小 | 866 aa / 101.3 kDa |
| UniProt ID | Q9BXJ9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nuclear bodies, Vesicles, Microtubules, Cytokin; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 866 aa / 101.3 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=52 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=89.4; PDB: 6C95, 6C9M, 6PPL, 6PW9, 9F1B, 9F1C, 9F1D |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR021183, IPR011990, IPR019734; Pfam: PF12569, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nuclear bodies, Vesicles, Microtubules, Cytokinetic bridge, Mitotic spindle, Primary cilium | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- NatA complex (GO:0031415)
- nuclear body (GO:0016604)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 52 |
| PubMed broad count | 90 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GA19, NARG1, NATH, TBDN100 |

**关键文献**:
1. Targeted sequencing identifies 91 neurodevelopmental-disorder risk genes with autism and developmental-disability biases.. *Nature genetics*. PMID: 28191889
2. Expanding the phenotypic spectrum of NAA10-related neurodevelopmental syndrome and NAA15-related neurodevelopmental syndrome.. *European journal of human genetics : EJHG*. PMID: 37130971
3. Truncating Variants in NAA15 Are Associated with Variable Levels of Intellectual Disability, Autism Spectrum Disorder, and Congenital Anomalies.. *American journal of human genetics*. PMID: 29656860
4. Naa15 Haploinsufficiency and De Novo Missense Variants Associate With Neurodevelopmental Disorders and Interfere With Neurogenesis and Neuron Development.. *Autism research : official journal of the International Society for Autism Research*. PMID: 39825710
5. Variants in NAA15 cause pediatric hypertrophic cardiomyopathy.. *American journal of medical genetics. Part A*. PMID: 33103328

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.4 |
| 高置信度残基 (pLDDT>90) 占比 | 77.5% |
| 置信残基 (pLDDT 70-90) 占比 | 11.9% |
| 中等置信 (pLDDT 50-70) 占比 | 5.3% |
| 低置信 (pLDDT<50) 占比 | 5.3% |
| 有序区域 (pLDDT>70) 占比 | 89.4% |
| 可用 PDB 条目 | 6C95, 6C9M, 6PPL, 6PW9, 9F1B, 9F1C, 9F1D, 9FPZ, 9FQ0, 9QQB |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（6C95, 6C9M, 6PPL, 6PW9, 9F1B, 9F1C, 9F1D, 9FPZ, 9FQ0, 9QQB）+ AlphaFold极高置信度预测（pLDDT=89.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR021183, IPR011990, IPR019734; Pfam: PF12569, PF13181 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NAA10 | 0.999 | 0.995 | — |
| HYPK | 0.999 | 0.985 | — |
| NAA50 | 0.999 | 0.996 | — |
| NAA11 | 0.997 | 0.851 | — |
| NAA25 | 0.993 | 0.000 | — |
| NAA20 | 0.991 | 0.199 | — |
| NAA16 | 0.982 | 0.821 | — |
| NAA35 | 0.979 | 0.000 | — |
| NAA30 | 0.979 | 0.000 | — |
| NAA38 | 0.952 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q811Z9 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| C901 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| dHYPK | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TNIK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EBI-1257125 | psi-mi:"MI:0096"(pull down) | pubmed:19463016|imex:IM-17246 |
| EBI-6249674 | psi-mi:"MI:0096"(pull down) | pubmed:22623228|imex:IM-17422 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.4 + PDB: 6C95, 6C9M, 6PPL, 6PW9, 9F1B,  | pLDDT=89.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol; 额外: Nuclear bodies, Vesicles, Microtubule | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. NAA15 — N-alpha-acetyltransferase 15, NatA auxiliary subunit，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小866 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 52 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BXJ9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164134-NAA15/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NAA15
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BXJ9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
