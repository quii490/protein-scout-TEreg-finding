---
type: protein-evaluation
gene: "MEIS2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MEIS2 — REJECTED (研究热度过高 (PubMed strict=209，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MEIS2 / MRG1 |
| 蛋白名称 | Homeobox protein Meis2 |
| 蛋白大小 | 477 aa / 51.8 kDa |
| UniProt ID | O14770 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm, perinuclear region |
| 蛋白大小 | 10/10 | ×1 | 10 | 477 aa / 51.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=209 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.0; PDB: 3K2A, 4XRM, 5BNG, 5EG0 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR009057, IPR008422, IPR032453, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Nucleus; Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 209 |
| PubMed broad count | 314 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MRG1 |

**关键文献**:
1. Human Genetics of Ventricular Septal Defect.. *Advances in experimental medicine and biology*. PMID: 38884729
2. Super-enhancer-driven IRF2BP2 enhances ALK activity and promotes neuroblastoma cell proliferation.. *Neuro-oncology*. PMID: 38864832
3. Crosstalk between liver sinusoidal endothelial cells and hepatocytes via IL-1α-IL1R1 axis exacerbates ischaemia/reperfusion injury in aged livers.. *Gut*. PMID: 41062182
4. Gene expression profiles and protein-protein interaction networks in neuroblastoma with MEIS2 depletion.. *Journal of B.U.ON. : official journal of the Balkan Union of Oncology*. PMID: 33277872
5. Fusion oncoproteins and cooperating mutations define disease phenotypes in NUP98-rearranged leukemia.. *Blood*. PMID: 40700635

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.0 |
| 高置信度残基 (pLDDT>90) 占比 | 22.9% |
| 置信残基 (pLDDT 70-90) 占比 | 11.5% |
| 中等置信 (pLDDT 50-70) 占比 | 19.1% |
| 低置信 (pLDDT<50) 占比 | 46.5% |
| 有序区域 (pLDDT>70) 占比 | 34.4% |
| 可用 PDB 条目 | 3K2A, 4XRM, 5BNG, 5EG0 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=62.0），有序残基占 34.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR009057, IPR008422, IPR032453, IPR050224; Pfam: PF05920, PF16493 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MEIS1 | 0.990 | 0.982 | — |
| PBX1 | 0.987 | 0.925 | — |
| PBX2 | 0.964 | 0.909 | — |
| PBX3 | 0.945 | 0.912 | — |
| HOXB13 | 0.927 | 0.905 | — |
| DLX3 | 0.922 | 0.903 | — |
| MAB21L1 | 0.872 | 0.836 | — |
| LMX1B | 0.872 | 0.827 | — |
| PBX4 | 0.863 | 0.801 | — |
| MAB21L2 | 0.850 | 0.818 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000453793.1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| Hoxa13 | psi-mi:"MI:0018"(two hybrid) | pubmed:15617687|imex:IM-19599 |
| rpoD | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| OSGIN1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| PBX1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PTK6 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SCT | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TIMM10B | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| KRTAP6-1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MCCD1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.0 + PDB: 3K2A, 4XRM, 5BNG, 5EG0 | pLDDT=62.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, perinuclear region / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. MEIS2 — Homeobox protein Meis2，研究基础较多，新颖性有限。
2. 蛋白大小477 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 209 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 209 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14770
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134138-MEIS2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MEIS2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14770
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
