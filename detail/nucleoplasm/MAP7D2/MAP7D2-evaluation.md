---
type: protein-evaluation
gene: "MAP7D2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAP7D2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAP7D2 |
| 蛋白名称 | MAP7 domain-containing protein 2 |
| 蛋白大小 | 732 aa / 82.0 kDa |
| UniProt ID | Q96T17 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 10/10 | ×1 | 10 | 732 aa / 82.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051483, IPR008604; Pfam: PF05672 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Midbody; Cytoplasm, cytoskeleton... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axon (GO:0030424)
- centrosome (GO:0005813)
- microtubule (GO:0005874)
- microtubule cytoskeleton (GO:0015630)
- midbody (GO:0030496)
- neuron projection (GO:0043005)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Map7D2 and Map7D1 facilitate microtubule stabilization through distinct mechanisms in neuronal cells.. *Life science alliance*. PMID: 35470240
2. Analysis of cancer-promoting genes related to chemotherapy resistance in esophageal squamous cell carcinoma.. *Annals of translational medicine*. PMID: 35282117
3. MAP7D2 reduces CD8(+) cytotoxic T lymphocyte infiltration through MYH9-HMGB1 axis in colorectal cancer.. *Molecular therapy : the journal of the American Society of Gene Therapy*. PMID: 36081350
4. MAP7D2 Localizes to the Proximal Axon and Locally Promotes Kinesin-1-Mediated Cargo Transport into the Axon.. *Cell reports*. PMID: 30784582
5. Molecular insights into gender-specific differences in rheumatoid arthritis: A study using high-throughput sequencing and Mendelian randomization.. *Medicine*. PMID: 40550064

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.3 |
| 高置信度残基 (pLDDT>90) 占比 | 18.6% |
| 置信残基 (pLDDT 70-90) 占比 | 17.1% |
| 中等置信 (pLDDT 50-70) 占比 | 18.3% |
| 低置信 (pLDDT<50) 占比 | 46.0% |
| 有序区域 (pLDDT>70) 占比 | 35.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=62.3），有序残基占 35.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051483, IPR008604; Pfam: PF05672 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NUTM2G | 0.590 | 0.000 | — |
| RTL9 | 0.556 | 0.058 | — |
| TRIM46 | 0.519 | 0.000 | — |
| KIF2A | 0.519 | 0.497 | — |
| TRIM36 | 0.496 | 0.394 | — |
| BCLAF3 | 0.492 | 0.000 | — |
| MAPT | 0.468 | 0.292 | — |
| NUGGC | 0.454 | 0.045 | — |
| EIF1AY | 0.451 | 0.046 | — |
| SCOC | 0.432 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| OLFML3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SMC2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| DHRS2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PLEKHA7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-25739|pubmed:28877994 |
| IL17RA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| P4HA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SIRT6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EFNB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FHL3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ECI2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.3 + PDB: 无 | pLDDT=62.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MAP7D2 — MAP7 domain-containing protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小732 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=62.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96T17
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184368-MAP7D2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAP7D2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96T17
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
