---
type: protein-evaluation
gene: "GPER1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPER1 — REJECTED (研究热度过高 (PubMed strict=491，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPER1 / CEPR, CMKRL2, DRY12, GPER, GPR30 |
| 蛋白名称 | G-protein coupled estrogen receptor 1 |
| 蛋白大小 | 375 aa / 42.2 kDa |
| UniProt ID | Q99527 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Nucleoplasm, Vesicles, Cytosol; UniProt: Nucleus; Cytoplasm; Cytoplasm, perinuclear region; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 375 aa / 42.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=491 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=79.1; PDB: 8XOF, 8XOG, 8XOH, 8XOI, 8XOJ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000276, IPR017452, IPR047143; Pfam: PF00001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm, Vesicles, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, perinuclear region; Cytoplasm, cytoskeleton; Cell membrane; Basolater... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axon (GO:0030424)
- axon terminus (GO:0043679)
- cytoplasm (GO:0005737)
- cytoplasmic vesicle membrane (GO:0030659)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- dendritic shaft (GO:0043198)
- dendritic spine head (GO:0044327)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 491 |
| PubMed broad count | 1501 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CEPR, CMKRL2, DRY12, GPER, GPR30 |

**关键文献**:
1. Estrogen receptor signaling mechanisms.. *Advances in protein chemistry and structural biology*. PMID: 31036290
2. Role of estrogen receptors in health and disease.. *Frontiers in endocrinology*. PMID: 36060947
3. Estrogen receptor signaling and targets: Bones, breasts and brain (Review).. *Molecular medicine reports*. PMID: 38904201
4. G protein-coupled estrogen receptor activates PI3K/AKT/mTOR signaling to suppress ferroptosis via SREBP1/SCD1-mediated lipogenesis.. *Molecular medicine (Cambridge, Mass.)*. PMID: 38383297
5. Activation of GPER1 in macrophages ameliorates UUO-induced renal fibrosis.. *Cell death & disease*. PMID: 38086848

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.1 |
| 高置信度残基 (pLDDT>90) 占比 | 41.9% |
| 置信残基 (pLDDT 70-90) 占比 | 29.6% |
| 中等置信 (pLDDT 50-70) 占比 | 15.5% |
| 低置信 (pLDDT<50) 占比 | 13.1% |
| 有序区域 (pLDDT>70) 占比 | 71.5% |
| 可用 PDB 条目 | 8XOF, 8XOG, 8XOH, 8XOI, 8XOJ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（8XOF, 8XOG, 8XOH, 8XOI, 8XOJ）+ AlphaFold极高置信度预测（pLDDT=79.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000276, IPR017452, IPR047143; Pfam: PF00001 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ESR1 | 0.953 | 0.292 | — |
| SRC | 0.948 | 0.000 | — |
| ESR2 | 0.943 | 0.000 | — |
| GNAS | 0.919 | 0.000 | — |
| PTK2 | 0.910 | 0.000 | — |
| GPR62 | 0.909 | 0.000 | — |
| GPR61 | 0.902 | 0.000 | — |
| EGFR | 0.843 | 0.000 | — |
| AGT | 0.810 | 0.000 | — |
| NPY | 0.758 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| A0A0F7RKM4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| FSHR | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:33299978|imex:IM-29784 |
| LHCGR | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:33299978|imex:IM-29784 |
| RAMP3 | psi-mi:"MI:0947"(bead aggregation assay) | pubmed:39083597|imex:IM-30383 |
| RAMP1 | psi-mi:"MI:0947"(bead aggregation assay) | pubmed:39083597|imex:IM-30383 |
| RAMP2 | psi-mi:"MI:0947"(bead aggregation assay) | pubmed:39083597|imex:IM-30383 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.1 + PDB: 8XOF, 8XOG, 8XOH, 8XOI, 8XOJ | pLDDT=79.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, perinuclear region; / Nucleoli; 额外: Nucleoplasm, Vesicles, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

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
1. GPER1 — G-protein coupled estrogen receptor 1，研究基础较多，新颖性有限。
2. 蛋白大小375 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 491 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 491 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99527
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164850-GPER1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPER1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99527
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
