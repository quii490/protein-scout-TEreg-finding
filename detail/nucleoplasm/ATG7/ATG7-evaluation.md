---
type: protein-evaluation
gene: "ATG7"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ATG7 — REJECTED (研究热度过高 (PubMed strict=2261，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ATG7 / APG7L |
| 蛋白名称 | Ubiquitin-like modifier-activating enzyme ATG7 |
| 蛋白大小 | 703 aa / 78.0 kDa |
| UniProt ID | O95352 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoplasm, Plasma membrane, Connecting piece,; UniProt: Cytoplasm; Preautophagosomal structure |
| 蛋白大小 | 10/10 | ×1 | 10 | 703 aa / 78.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2261 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR006285, IPR032197, IPR042522, IPR042523, IPR045 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.0/180** | |
| **归一化总分** | | | **42.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Plasma membrane, Connecting piece, Flagellar centriole, Mid piece | Approved |
| UniProt | Cytoplasm; Preautophagosomal structure | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axoneme (GO:0005930)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular region (GO:0005576)
- ficolin-1-rich granule lumen (GO:1904813)
- phagophore assembly site (GO:0000407)
- secretory granule lumen (GO:0034774)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2261 |
| PubMed broad count | 3636 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: APG7L |

**关键文献**:
1. The UFM1 system regulates ER-phagy through the ufmylation of CYB5R3.. *Nature communications*. PMID: 36543799
2. m(6)A mRNA methylation controls autophagy and adipogenesis by targeting Atg5 and Atg7.. *Autophagy*. PMID: 31451060
3. Deacetylation of ATG7 drives the induction of macroautophagy and LC3-associated microautophagy.. *Autophagy*. PMID: 37999993
4. Ablation of endothelial Atg7 inhibits ischemia-induced angiogenesis by upregulating Stat1 that suppresses Hif1a expression.. *Autophagy*. PMID: 36300763
5. TRIM7/RNF90 promotes autophagy via regulation of ATG7 ubiquitination during L. monocytogenes infection.. *Autophagy*. PMID: 36576150

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.6 |
| 高置信度残基 (pLDDT>90) 占比 | 66.4% |
| 置信残基 (pLDDT 70-90) 占比 | 23.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.8% |
| 低置信 (pLDDT<50) 占比 | 5.0% |
| 有序区域 (pLDDT>70) 占比 | 90.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.6，有序区 90.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006285, IPR032197, IPR042522, IPR042523, IPR045886; Pfam: PF16420, PF00899 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ATG12 | 0.999 | 0.922 | — |
| GABARAP | 0.999 | 0.942 | — |
| GABARAPL2 | 0.999 | 0.916 | — |
| ATG5 | 0.999 | 0.252 | — |
| ATG10 | 0.999 | 0.637 | — |
| ATG3 | 0.999 | 0.990 | — |
| GABARAPL1 | 0.999 | 0.870 | — |
| MAP1LC3A | 0.998 | 0.895 | — |
| MAP1LC3B | 0.998 | 0.913 | — |
| FOXO1 | 0.998 | 0.739 | — |

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
| 三维结构 | AlphaFold pLDDT=87.6 + PDB: 无 | pLDDT=87.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Preautophagosomal structure / Cytosol; 额外: Nucleoplasm, Plasma membrane, Connect | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ATG7 — Ubiquitin-like modifier-activating enzyme ATG7，研究基础较多，新颖性有限。
2. 蛋白大小703 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2261 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2261 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95352
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197548-ATG7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ATG7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95352
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
