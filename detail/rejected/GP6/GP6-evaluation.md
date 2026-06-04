---
type: protein-evaluation
gene: "GP6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GP6 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=221，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GP6 |
| 蛋白名称 | Platelet glycoprotein VI |
| 蛋白大小 | 339 aa / 36.9 kDa |
| UniProt ID | Q9HCN6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Plasma membrane; UniProt: Cell membrane; Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 339 aa / 36.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=221 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.0; PDB: 2GI7, 5OU7, 5OU8, 5OU9, 7NMU, 7R58 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036179, IPR013783, IPR050412, IPR003599, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **74.0/180** | |
| **归一化总分** | | | **41.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane | Supported |
| UniProt | Cell membrane; Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell surface (GO:0009986)
- extracellular exosome (GO:0070062)
- extracellular matrix (GO:0031012)
- membrane raft (GO:0045121)
- plasma membrane (GO:0005886)
- tetraspanin-enriched microdomain (GO:0097197)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 221 |
| PubMed broad count | 612 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Urinary proteomics identifies distinct immunological profiles of sepsis associated AKI sub-phenotypes.. *Critical care (London, England)*. PMID: 39695715
2. Machine learning reveals sex-biased platelet-associated molecular signatures in systemic lupus erythematosus.. *Immunology letters*. PMID: 41506349
3. Variability of GP6 gene in patients with sticky platelet syndrome and deep venous thrombosis and/or pulmonary embolism.. *Blood coagulation & fibrinolysis : an international journal in haemostasis and thrombosis*. PMID: 22821001
4. hTERT and IGF-1R Proteins Expression in Response to Treatment in Patients with HPV Alpha 9-Positive Cervical Cancer.. *Radiation research*. PMID: 36888727
5. Genetic variations of the GP6 regulatory region in patients with sticky platelet syndrome and miscarriage.. *Expert review of hematology*. PMID: 26308704

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.0 |
| 高置信度残基 (pLDDT>90) 占比 | 54.6% |
| 置信残基 (pLDDT 70-90) 占比 | 7.4% |
| 中等置信 (pLDDT 50-70) 占比 | 13.6% |
| 低置信 (pLDDT<50) 占比 | 24.5% |
| 有序区域 (pLDDT>70) 占比 | 62.0% |
| 可用 PDB 条目 | 2GI7, 5OU7, 5OU8, 5OU9, 7NMU, 7R58 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2GI7, 5OU7, 5OU8, 5OU9, 7NMU, 7R58）+ AlphaFold极高置信度预测（pLDDT=76.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036179, IPR013783, IPR050412, IPR003599, IPR003598; Pfam: PF13895, PF13927 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FCER1G | 0.999 | 0.510 | — |
| LYN | 0.997 | 0.798 | — |
| VWF | 0.997 | 0.000 | — |
| FYN | 0.996 | 0.648 | — |
| ITGA2 | 0.976 | 0.071 | — |
| LGALS3 | 0.974 | 0.048 | — |
| GP5 | 0.961 | 0.095 | — |
| S100A10 | 0.954 | 0.000 | — |
| COL8A2 | 0.949 | 0.000 | — |
| GP1BA | 0.946 | 0.095 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FCER1G | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:9280292 |
| LYN | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:1715582 |
| YES1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:1715582 |
| FYN | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:1715582 |
| H3-4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.0 + PDB: 2GI7, 5OU7, 5OU8, 5OU9, 7NMU,  | pLDDT=76.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Cell membrane / Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GP6 — Platelet glycoprotein VI，研究基础较多，新颖性有限。
2. 蛋白大小339 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 221 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HCN6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000088053-GP6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GP6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HCN6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
