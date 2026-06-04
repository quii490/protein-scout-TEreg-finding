---
type: protein-evaluation
gene: "DEPTOR"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DEPTOR — REJECTED (研究热度过高 (PubMed strict=224，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DEPTOR / DEPDC6 |
| 蛋白名称 | DEP domain-containing mTOR-interacting protein |
| 蛋白大小 | 409 aa / 46.3 kDa |
| UniProt ID | Q8TB45 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Mitochondria; 额外: Nucleoplasm, Nuclear bodies; UniProt: Lysosome membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 409 aa / 46.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=224 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=79.7; PDB: 7DKL, 7OWG, 7PE7, 7PE8, 7PE9, 7PEA, 7PEB |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000591, IPR037335, IPR037336, IPR051832, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **82.0/180** | |
| **归一化总分** | | | **45.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoplasm, Nuclear bodies | Approved |
| UniProt | Lysosome membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- lysosomal membrane (GO:0005765)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 224 |
| PubMed broad count | 321 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DEPDC6 |

**关键文献**:
1. How autophagy controls the intestinal epithelial barrier.. *Autophagy*. PMID: 33906557
2. Lipotoxicity-induced STING1 activation stimulates MTORC1 and restricts hepatic lipophagy.. *Autophagy*. PMID: 34382907
3. DEPTOR suppresses lymphomagenesis by promoting EGFR degradation via HUWE1 E3 ligase.. *Cell death and differentiation*. PMID: 40169856
4. Deptor: not only a mTOR inhibitor.. *Journal of experimental & clinical cancer research : CR*. PMID: 28086984
5. PUM1 Promotes Tumor Progression by Activating DEPTOR-Meditated Glycolysis in Gastric Cancer.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 37469018

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.7 |
| 高置信度残基 (pLDDT>90) 占比 | 55.0% |
| 置信残基 (pLDDT 70-90) 占比 | 21.5% |
| 中等置信 (pLDDT 50-70) 占比 | 1.7% |
| 低置信 (pLDDT<50) 占比 | 21.8% |
| 有序区域 (pLDDT>70) 占比 | 76.5% |
| 可用 PDB 条目 | 7DKL, 7OWG, 7PE7, 7PE8, 7PE9, 7PEA, 7PEB, 7PEC, 7PED |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（7DKL, 7OWG, 7PE7, 7PE8, 7PE9, 7PEA, 7PEB, 7PEC, 7PED）+ AlphaFold极高置信度预测（pLDDT=79.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000591, IPR037335, IPR037336, IPR051832, IPR001478; Pfam: PF00610 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AKT1S1 | 0.999 | 0.000 | — |
| MAPKAP1 | 0.999 | 0.800 | — |
| RPTOR | 0.999 | 0.897 | — |
| MTOR | 0.999 | 0.972 | — |
| RICTOR | 0.999 | 0.852 | — |
| MLST8 | 0.999 | 0.879 | — |
| PRR5 | 0.998 | 0.000 | — |
| TTI1 | 0.995 | 0.052 | — |
| RPS6KB1 | 0.991 | 0.292 | — |
| RHEB | 0.988 | 0.107 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MTOR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12190|pubmed:19446321 |
| RPTOR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12190|pubmed:19446321 |
| RICTOR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12190|pubmed:19446321 |
| MLST8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12190|pubmed:19446321 |
| ANKRD11 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TRAF1 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| CCDC110 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| ATP2B4 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| CYSLTR2 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.7 + PDB: 7DKL, 7OWG, 7PE7, 7PE8, 7PE9,  | pLDDT=79.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Lysosome membrane / Mitochondria; 额外: Nucleoplasm, Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. DEPTOR — DEP domain-containing mTOR-interacting protein，研究基础较多，新颖性有限。
2. 蛋白大小409 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 224 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 224 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TB45
- Protein Atlas: https://www.proteinatlas.org/ENSG00000155792-DEPTOR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DEPTOR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TB45
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
