---
type: protein-evaluation
gene: "CRYAB"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CRYAB — REJECTED (研究热度过高 (PubMed strict=502，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRYAB / CRYA2, HSPB5 |
| 蛋白名称 | Alpha-crystallin B chain |
| 蛋白大小 | 175 aa / 20.2 kDa |
| UniProt ID | P02511 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Plasma membrane, Cytosol; UniProt: Cytoplasm; Nucleus; Secreted; Lysosome |
| 蛋白大小 | 8/10 | x1 | 8 | 175 aa / 20.2 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=502 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=75.8; PDB: 2KLR, 2N0K, 2WJ7, 2Y1Y, 2Y1Z, 2Y22, 2YGD |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR002068, IPR037882, IPR055269, IPR001436, IPR003 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.5/180** | |
| **归一化总分** | | | **50.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol | Enhanced |
| UniProt | Cytoplasm; Nucleus; Secreted; Lysosome | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- actin filament bundle (GO:0032432)
- axon (GO:0030424)
- cardiac myofibril (GO:0097512)
- cell surface (GO:0009986)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendritic spine (GO:0043197)
- extracellular exosome (GO:0070062)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 502 |
| PubMed broad count | 810 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CRYA2, HSPB5 |

**关键文献**:
1. Single-cell analysis of breast cancer metastasis reveals epithelial-mesenchymal plasticity signatures associated with poor outcomes.. *The Journal of clinical investigation*. PMID: 39225101
2. [Myofibrillar myopaathy].. *Rinsho shinkeigaku = Clinical neurology*. PMID: 24291893
3. Mutation of CRYAB encoding a conserved mitochondrial chaperone and antiapoptotic protein causes hereditary optic atrophy.. *JCI insight*. PMID: 39561005
4. TANGO2 binds crystallin alpha B and its loss causes desminopathy.. *Nature communications*. PMID: 40480980
5. Mitophagy Facilitates Cytosolic Proteostasis to Preserve Cardiac Function.. *bioRxiv : the preprint server for biology*. PMID: 39651239

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.8 |
| 高置信度残基 (pLDDT>90) 占比 | 39.4% |
| 置信残基 (pLDDT 70-90) 占比 | 22.3% |
| 中等置信 (pLDDT 50-70) 占比 | 21.7% |
| 低置信 (pLDDT<50) 占比 | 16.6% |
| 有序区域 (pLDDT>70) 占比 | 61.7% |
| 可用 PDB 条目 | 2KLR, 2N0K, 2WJ7, 2Y1Y, 2Y1Z, 2Y22, 2YGD, 3J07, 3L1G, 3SGM |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构 + AlphaFold极高置信度（pLDDT=75.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002068, IPR037882, IPR055269, IPR001436, IPR003090; Pfam: PF00525, PF00011 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CRYAA | 0.996 | 0.927 | — |
| BAG3 | 0.944 | 0.562 | — |
| HSPB1 | 0.940 | 0.875 | — |
| CRYBB2 | 0.939 | 0.622 | — |
| CRYGS | 0.924 | 0.601 | — |
| CRYGD | 0.924 | 0.722 | — |
| HSPB2 | 0.921 | 0.785 | — |
| CRYBA1 | 0.911 | 0.617 | — |
| APP | 0.898 | 0.784 | — |
| SNCA | 0.863 | 0.784 | — |

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
| 三维结构 | AlphaFold pLDDT=75.8 + PDB: 2KLR, 2N0K, 2WJ7, 2Y1Y, 2Y1Z,  | pLDDT=75.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Secreted; Lysosome / Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CRYAB -- Alpha-crystallin B chain，研究基础较多，新颖性有限。
2. 蛋白大小175 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 502 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 502 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P02511
- Protein Atlas: https://www.proteinatlas.org/ENSG00000109846-CRYAB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRYAB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P02511
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
