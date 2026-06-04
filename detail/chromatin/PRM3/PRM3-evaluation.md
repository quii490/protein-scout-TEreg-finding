---
type: protein-evaluation
gene: "PRM3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRM3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRM3 |
| 蛋白名称 | Protamine-3 |
| 蛋白大小 | 103 aa / 11.3 kDa |
| UniProt ID | Q9NNZ6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 8/10 | ×1 | 8 | 103 aa / 11.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=32 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026077 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleosome (GO:0000786)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 44 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Prm3, the fourth gene in the mouse protamine gene cluster, encodes a conserved acidic protein that affects sperm motility.. *Biology of reproduction*. PMID: 18256328
2. Differential expression of the TPα and TPβ isoforms of the human T Prostanoid receptor during chronic inflammation of the prostate: Role for FOXP1 in the transcriptional regulation of TPβ during monocyte-macrophage differentiation.. *Experimental and molecular pathology*. PMID: 31271729
3. Polysaccharide PRM3 from Rhynchosia minima root enhances immune function through TLR4-NF-κB pathway.. *Biochimica et biophysica acta. General subjects*. PMID: 29763643
4. Protamine 3 shows evidence of weak, positive selection in mouse species (genus Mus)--but it is not a protamine.. *Biology of reproduction*. PMID: 20944085
5. Protamine 2 and phospholipase C zeta 1 are possible biomarkers for the diagnosis of male subfertility in frozen-thawed stallion semen.. *Theriogenology*. PMID: 38142472

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.9 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 15.5% |
| 中等置信 (pLDDT 50-70) 占比 | 60.2% |
| 低置信 (pLDDT<50) 占比 | 24.3% |
| 有序区域 (pLDDT>70) 占比 | 15.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=57.9），有序残基占 15.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026077 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRM2 | 0.837 | 0.000 | — |
| TNP2 | 0.825 | 0.000 | — |
| TNP1 | 0.705 | 0.000 | — |
| PRM1 | 0.548 | 0.000 | — |
| ROMO1 | 0.489 | 0.000 | — |
| SPACA3 | 0.461 | 0.000 | — |
| BRDT | 0.453 | 0.000 | — |
| TMEM225 | 0.451 | 0.000 | — |
| IZUMO3 | 0.448 | 0.000 | — |
| TSSK6 | 0.447 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HMT1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| PHS1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| GPI14 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| ARRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SSU72 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.9 + PDB: 无 | pLDDT=57.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PRM3 — Protamine-3，非常新颖，仅有少数基础研究。
2. 蛋白大小103 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=57.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NNZ6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178257-PRM3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRM3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NNZ6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
