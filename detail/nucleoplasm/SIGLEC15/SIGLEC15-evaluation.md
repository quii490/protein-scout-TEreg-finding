---
type: protein-evaluation
gene: "SIGLEC15"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SIGLEC15 — REJECTED (研究热度过高 (PubMed strict=110，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SIGLEC15 / CD33L3 |
| 蛋白名称 | Sialic acid-binding Ig-like lectin 15 |
| 蛋白大小 | 328 aa / 35.7 kDa |
| UniProt ID | Q6ZMC9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Golgi apparatus; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 328 aa / 35.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=110 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=78.4; PDB: 7ZOZ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007110, IPR036179, IPR013783, IPR003599, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **74.5/180** | |
| **归一化总分** | | | **41.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- plasma membrane (GO:0005886)
- protein-containing complex (GO:0032991)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 110 |
| PubMed broad count | 212 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CD33L3 |

**关键文献**:
1. Osteoclast differentiation by RANKL and OPG signaling pathways.. *Journal of bone and mineral metabolism*. PMID: 33079279
2. Evasion of immunosurveillance by the upregulation of Siglec15 in bladder cancer.. *Journal of hematology & oncology*. PMID: 39609852
3. Predicting ovarian cancer prognosis and immunotherapy response through siglec15 and PD-L1 expression analysis.. *Translational oncology*. PMID: 41076961
4. Emerging strategies in targeting tumor-resident myeloid cells for cancer immunotherapy.. *Journal of hematology & oncology*. PMID: 36031601
5. Siglec15 promotes the migration of thyroid carcinoma cells by enhancing the EGFR protein stability.. *Glycobiology*. PMID: 37129515

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.4 |
| 高置信度残基 (pLDDT>90) 占比 | 57.0% |
| 置信残基 (pLDDT 70-90) 占比 | 12.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.3% |
| 低置信 (pLDDT<50) 占比 | 23.5% |
| 有序区域 (pLDDT>70) 占比 | 69.2% |
| 可用 PDB 条目 | 7ZOZ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=78.4，有序区 69.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007110, IPR036179, IPR013783, IPR003599, IPR013106; Pfam: PF07686 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TYROBP | 0.978 | 0.000 | — |
| EEF1A2 | 0.889 | 0.000 | — |
| SIGLEC1 | 0.759 | 0.126 | — |
| CD22 | 0.750 | 0.126 | — |
| SIGLEC7 | 0.669 | 0.126 | — |
| MAG | 0.660 | 0.126 | — |
| SIGLEC11 | 0.643 | 0.126 | — |
| HCST | 0.624 | 0.000 | — |
| SIGLEC8 | 0.624 | 0.126 | — |
| FCER1G | 0.605 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=78.4 + PDB: 7ZOZ | pLDDT=78.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm, Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SIGLEC15 — Sialic acid-binding Ig-like lectin 15，研究基础较多，新颖性有限。
2. 蛋白大小328 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 110 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 110 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZMC9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197046-SIGLEC15/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SIGLEC15
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZMC9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
