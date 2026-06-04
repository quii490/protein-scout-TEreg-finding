---
type: protein-evaluation
gene: "BLM"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BLM — REJECTED (研究热度过高 (PubMed strict=2194，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BLM / RECQ2, RECQL3 |
| 蛋白名称 | RecQ-like DNA helicase BLM |
| 蛋白大小 | 1417 aa / 159.0 kDa |
| UniProt ID | P54132 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1417 aa / 159.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2194 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.5; PDB: 2KV2, 2MH9, 2RRD, 3WE2, 3WE3, 4CDG, 4CGZ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012532, IPR032439, IPR032437, IPR011545, IPR002 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.5/180** | |
| **归一化总分** | | | **42.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome (GO:0005694)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- lateral element (GO:0000800)
- nuclear chromosome (GO:0000228)
- nuclear matrix (GO:0016363)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2194 |
| PubMed broad count | 6525 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RECQ2, RECQL3 |

**关键文献**:
1. Calpain-1 Up-Regulation Promotes Bleomycin-Induced Pulmonary Fibrosis by Activating Ferroptosis.. *The American journal of pathology*. PMID: 39326733
2. Immunodeficiency in Bloom's Syndrome.. *Journal of clinical immunology*. PMID: 29098565
3. [Bloom syndrome].. *Nihon rinsho. Japanese journal of clinical medicine*. PMID: 10921324
4. Peroxiredoxin 1 mediates bleomycin-induced acute lung injury in mice via macrophage NOD1/NF-κB axis.. *Respiratory research*. PMID: 41618391
5. Contribution of the STING in macrophages to the pulmonary inflammation and fibrosis.. *International immunopharmacology*. PMID: 41592393

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.5 |
| 高置信度残基 (pLDDT>90) 占比 | 29.6% |
| 置信残基 (pLDDT 70-90) 占比 | 16.8% |
| 中等置信 (pLDDT 50-70) 占比 | 2.7% |
| 低置信 (pLDDT<50) 占比 | 50.9% |
| 有序区域 (pLDDT>70) 占比 | 46.4% |
| 可用 PDB 条目 | 2KV2, 2MH9, 2RRD, 3WE2, 3WE3, 4CDG, 4CGZ, 4O3M, 5LUP, 5MK5 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=60.5），有序残基占 46.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012532, IPR032439, IPR032437, IPR011545, IPR002464; Pfam: PF08072, PF16204, PF16202 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FANCM | 0.999 | 0.999 | — |
| RPA1 | 0.999 | 0.998 | — |
| FANCA | 0.999 | 0.994 | — |
| FANCG | 0.999 | 0.994 | — |
| RMI1 | 0.999 | 0.996 | — |
| TOP3A | 0.999 | 0.998 | — |
| MLH1 | 0.999 | 0.996 | — |
| RAD51 | 0.998 | 0.970 | — |
| EXO1 | 0.998 | 0.907 | — |
| RPA3 | 0.998 | 0.994 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TERF2 | psi-mi:"MI:0411"(enzyme linked immunosorbent assay | pubmed:12181313 |
| WRN | psi-mi:"MI:0411"(enzyme linked immunosorbent assay | pubmed:11919194 |
| RPA1 | psi-mi:"MI:0411"(enzyme linked immunosorbent assay | pubmed:15965237 |
| FEN1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:14688284 |
| BtbVII | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| dl | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| slam | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| mtDNA-helicase | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| pan | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| CG7696 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.5 + PDB: 2KV2, 2MH9, 2RRD, 3WE2, 3WE3,  | pLDDT=60.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BLM — RecQ-like DNA helicase BLM，研究基础较多，新颖性有限。
2. 蛋白大小1417 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 2194 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2194 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P54132
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197299-BLM/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BLM
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P54132
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
