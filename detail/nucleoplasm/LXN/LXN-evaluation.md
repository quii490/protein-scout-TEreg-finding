---
type: protein-evaluation
gene: "LXN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LXN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LXN |
| 蛋白名称 | Latexin |
| 蛋白大小 | 222 aa / 25.8 kDa |
| UniProt ID | Q9BS40 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 222 aa / 25.8 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=50 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=96.0; PDB: 2BO9 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR049897, IPR046350, IPR009684; Pfam: PF06907 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **107.0/180** | |
| **归一化总分** | | | **59.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- extracellular space (GO:0005615)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 50 |
| PubMed broad count | 187 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of the shared gene signatures and pathways between sarcopenia and type 2 diabetes mellitus.. *PloS one*. PMID: 35271662
2. Latexin deficiency limits foam cell formation and ameliorates atherosclerosis by promoting macrophage phenotype differentiation.. *Cell death & disease*. PMID: 39424784
3. Carboxypeptidase inhibitor Latexin (LXN) regulates intestinal organogenesis and intestinal remodeling involved in intestinal injury repair in mice.. *International journal of biological macromolecules*. PMID: 39208900
4. Latexin deficiency in mice up-regulates inflammation and aggravates colitis through HECTD1/Rps3/NF-κB pathway.. *Scientific reports*. PMID: 32555320
5. Premature renal epithelial cell senescence promoted by LXN/Rps3/p53 signaling pathway activation increases calcium oxalate crystal deposition by altering macrophage polarization.. *Frontiers in immunology*. PMID: 41112268

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.0 |
| 高置信度残基 (pLDDT>90) 占比 | 95.5% |
| 置信残基 (pLDDT 70-90) 占比 | 2.3% |
| 中等置信 (pLDDT 50-70) 占比 | 0.5% |
| 低置信 (pLDDT<50) 占比 | 1.8% |
| 有序区域 (pLDDT>70) 占比 | 97.8% |
| 可用 PDB 条目 | 2BO9 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=96.0，有序区 97.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR049897, IPR046350, IPR009684; Pfam: PF06907 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CPA4 | 0.996 | 0.946 | — |
| CPA2 | 0.809 | 0.000 | — |
| CPA1 | 0.669 | 0.000 | — |
| RPS3 | 0.642 | 0.292 | — |
| NTNG2 | 0.575 | 0.000 | — |
| DAB2IP | 0.556 | 0.000 | — |
| AGBL2 | 0.546 | 0.000 | — |
| GNG2 | 0.486 | 0.000 | — |
| CUX2 | 0.486 | 0.000 | — |
| PIR | 0.478 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000264265.3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NUDC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MAGEB2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CIRBP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PANK2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PHACTR3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PPM1A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CEP162 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| THRAP3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SOST | psi-mi:"MI:0096"(pull down) | pubmed:22206666|imex:IM-17213 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.0 + PDB: 2BO9 | pLDDT=96.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LXN — Latexin，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小222 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 50 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BS40
- Protein Atlas: https://www.proteinatlas.org/ENSG00000079257-LXN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LXN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BS40
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
