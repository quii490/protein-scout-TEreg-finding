---
type: protein-evaluation
gene: "EVC2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EVC2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EVC2 / LBN |
| 蛋白名称 | Limbin |
| 蛋白大小 | 1308 aa / 147.9 kDa |
| UniProt ID | Q86UK5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Microtubules, Cytokinetic bridge, Primary c; UniProt: Cell membrane; Cytoplasm, cytoskeleton, cilium basal body; C |
| 蛋白大小 | 5/10 | ×1 | 5 | 1308 aa / 147.9 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=88 篇 (≤100→2) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR022076, IPR026501; Pfam: PF12297 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Microtubules, Cytokinetic bridge, Primary cilium; 额外: Nucleoplasm, Primary cilium tip, Basal body, Cytosol | Approved |
| UniProt | Cell membrane; Cytoplasm, cytoskeleton, cilium basal body; Cell projection, cilium; Cell projection,... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- ciliary membrane (GO:0060170)
- cilium (GO:0005929)
- nucleus (GO:0005634)
- plasma membrane protein complex (GO:0098797)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 88 |
| PubMed broad count | 148 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LBN |

**关键文献**:
1. Human Genetics of Ventricular Septal Defect.. *Advances in experimental medicine and biology*. PMID: 38884729
2. Ellis-van Creveld Syndrome.. **. PMID: 37903214
3. Human-chimpanzee fused cells reveal cis-regulatory divergence underlying skeletal evolution.. *Nature genetics*. PMID: 33731941
4. EVC-EVC2 complex stability and ciliary targeting are regulated by modification with ubiquitin and SUMO.. *Frontiers in cell and developmental biology*. PMID: 37576597
5. Novel and recurrent EVC and EVC2 mutations in Ellis-van Creveld syndrome and Weyers acrofacial dyostosis.. *European journal of medical genetics*. PMID: 23220543

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.7 |
| 高置信度残基 (pLDDT>90) 占比 | 33.5% |
| 置信残基 (pLDDT 70-90) 占比 | 34.8% |
| 中等置信 (pLDDT 50-70) 占比 | 8.9% |
| 低置信 (pLDDT<50) 占比 | 22.9% |
| 有序区域 (pLDDT>70) 占比 | 68.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=72.7，有序区 68.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR022076, IPR026501; Pfam: PF12297 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EVC | 0.999 | 0.000 | — |
| SMO | 0.979 | 0.000 | — |
| EFCAB7 | 0.898 | 0.000 | — |
| IQCE | 0.884 | 0.000 | — |
| SUFU | 0.796 | 0.000 | — |
| STK32B | 0.762 | 0.000 | — |
| NSG1 | 0.749 | 0.000 | — |
| GLI2 | 0.749 | 0.000 | — |
| CRMP1 | 0.740 | 0.000 | — |
| STX18 | 0.701 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SRPRA | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| SPCS2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| STIP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| SRPRB | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| STX5 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| NUDCD3 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| SEC24B | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| TMX1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| HSPBP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| CDC37 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.7 + PDB: 无 | pLDDT=72.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Cytoplasm, cytoskeleton, cilium bas / Plasma membrane, Microtubules, Cytokinetic bridge, | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. EVC2 — Limbin，研究基础较多，新颖性有限。
2. 蛋白大小1308 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 88 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86UK5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173040-EVC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EVC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86UK5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
