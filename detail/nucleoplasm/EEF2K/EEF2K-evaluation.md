---
type: protein-evaluation
gene: "EEF2K"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EEF2K — REJECTED (研究热度过高 (PubMed strict=286，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EEF2K |
| 蛋白名称 | Eukaryotic elongation factor 2 kinase |
| 蛋白大小 | 725 aa / 82.1 kDa |
| UniProt ID | O00418 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 725 aa / 82.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=286 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=71.8; PDB: 5J8H, 5KS5, 6NX4, 7SHQ, 8FNY, 8FO6, 8GM4 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004166, IPR051852, IPR017400, IPR047588, IPR011 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **82.0/180** | |
| **归一化总分** | | | **45.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendritic spine (GO:0043197)
- glutamatergic synapse (GO:0098978)
- postsynaptic density (GO:0014069)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 286 |
| PubMed broad count | 482 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of a Novel Substrate for eEF2K and the AURKA-SOX8 as the Related Pathway in TNBC.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39950798
2. 16p12.2 Recurrent Deletion.. **. PMID: 25719193
3. Fluoxetine regulates eEF2 activity (phosphorylation) via HDAC1 inhibitory mechanism in an LPS-induced mouse model of depression.. *Journal of neuroinflammation*. PMID: 33526073
4. Design and Characterization of a Novel eEF2K Degrader with Potent Therapeutic Efficacy Against Triple-Negative Breast Cancer.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 38084501
5. PQBP1 promotes translational elongation and regulates hippocampal mGluR-LTD by suppressing eEF2 phosphorylation.. *Molecular cell*. PMID: 33662272

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.8 |
| 高置信度残基 (pLDDT>90) 占比 | 45.2% |
| 置信残基 (pLDDT 70-90) 占比 | 18.3% |
| 中等置信 (pLDDT 50-70) 占比 | 6.8% |
| 低置信 (pLDDT<50) 占比 | 29.7% |
| 有序区域 (pLDDT>70) 占比 | 63.5% |
| 可用 PDB 条目 | 5J8H, 5KS5, 6NX4, 7SHQ, 8FNY, 8FO6, 8GM4, 8GM5 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（5J8H, 5KS5, 6NX4, 7SHQ, 8FNY, 8FO6, 8GM4, 8GM5）+ AlphaFold极高置信度预测（pLDDT=71.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004166, IPR051852, IPR017400, IPR047588, IPR011009; Pfam: PF02816 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EEF2 | 0.999 | 0.292 | — |
| CALM3 | 0.987 | 0.927 | — |
| RPS6KB1 | 0.961 | 0.292 | — |
| CALM2 | 0.931 | 0.927 | — |
| CALM1 | 0.931 | 0.927 | — |
| PRKCA | 0.928 | 0.000 | — |
| PRKAA2 | 0.915 | 0.000 | — |
| PRKAG2 | 0.915 | 0.000 | — |
| PRKCB | 0.914 | 0.000 | — |
| PRKAA1 | 0.914 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BTRC | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| WDFY3 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| SRP9 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| ACACA | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| SRP14 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| RAE1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| FBXW11 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| EZR | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| FKBP6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.8 + PDB: 5J8H, 5KS5, 6NX4, 7SHQ, 8FNY,  | pLDDT=71.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EEF2K — Eukaryotic elongation factor 2 kinase，研究基础较多，新颖性有限。
2. 蛋白大小725 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 286 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 286 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00418
- Protein Atlas: https://www.proteinatlas.org/ENSG00000103319-EEF2K/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EEF2K
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00418
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
