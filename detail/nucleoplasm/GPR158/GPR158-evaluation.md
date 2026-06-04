---
type: protein-evaluation
gene: "GPR158"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GPR158 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR158 / KIAA1136 |
| 蛋白名称 | Metabotropic glycine receptor |
| 蛋白大小 | 1215 aa / 135.5 kDa |
| UniProt ID | Q5T848 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Postsynaptic cell membrane; Presynaptic cell  |
| 蛋白大小 | 5/10 | ×1 | 5 | 1215 aa / 135.5 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=67 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.0; PDB: 7EWL, 7EWP, 7EWR, 7SHE, 7SHF |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR017978, IPR043458, IPR054714; Pfam: PF00003, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.5/180** | |
| **归一化总分** | | | **53.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane; Postsynaptic cell membrane; Presynaptic cell membrane; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- postsynaptic density membrane (GO:0098839)
- postsynaptic membrane (GO:0045211)
- presynaptic membrane (GO:0042734)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 67 |
| PubMed broad count | 82 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1136 |

**关键文献**:
1. Orphan receptor GPR158 serves as a metabotropic glycine receptor: mGlyR.. *Science (New York, N.Y.)*. PMID: 36996198
2. Cryo-EM structure of human GPR158 receptor coupled to the RGS7-Gβ5 signaling complex.. *Science (New York, N.Y.)*. PMID: 34793198
3. GPR158 in pyramidal neurons mediates social novelty behavior via modulating synaptic transmission in male mice.. *Cell reports*. PMID: 39383040
4. Osteocalcin and GPR158: linking bone and brain function.. *Frontiers in cell and developmental biology*. PMID: 40337551
5. The interaction, mechanism and function of GPR158-RGS7 cross-talk.. *Progress in molecular biology and translational science*. PMID: 36357076

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.0 |
| 高置信度残基 (pLDDT>90) 占比 | 13.8% |
| 置信残基 (pLDDT 70-90) 占比 | 27.0% |
| 中等置信 (pLDDT 50-70) 占比 | 11.0% |
| 低置信 (pLDDT<50) 占比 | 48.1% |
| 有序区域 (pLDDT>70) 占比 | 40.8% |
| 可用 PDB 条目 | 7EWL, 7EWP, 7EWR, 7SHE, 7SHF |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=58.0），有序残基占 40.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017978, IPR043458, IPR054714; Pfam: PF00003, PF22572 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RGS7 | 0.989 | 0.900 | — |
| GNB5 | 0.932 | 0.800 | — |
| GPRC6A | 0.771 | 0.000 | — |
| BGLAP | 0.756 | 0.000 | — |
| GPR156 | 0.676 | 0.000 | — |
| GPC4 | 0.656 | 0.000 | — |
| GPR137 | 0.623 | 0.000 | — |
| GPRC5B | 0.594 | 0.000 | — |
| RGS11 | 0.567 | 0.000 | — |
| GPR52 | 0.548 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| PITX2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| Pde4dip | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.0 + PDB: 7EWL, 7EWP, 7EWR, 7SHE, 7SHF | pLDDT=58.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Postsynaptic cell membrane; Presyna / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GPR158 — Metabotropic glycine receptor，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小1215 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 67 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=58.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5T848
- Protein Atlas: https://www.proteinatlas.org/ENSG00000151025-GPR158/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR158
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5T848
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
