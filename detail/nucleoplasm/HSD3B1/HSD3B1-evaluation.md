---
type: protein-evaluation
gene: "HSD3B1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HSD3B1 — REJECTED (研究热度过高 (PubMed strict=416，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HSD3B1 / 3BH, HSDB3A |
| 蛋白名称 | 3 beta-hydroxysteroid dehydrogenase/Delta 5-->4-isomerase type 1 |
| 蛋白大小 | 373 aa / 42.3 kDa |
| UniProt ID | P14060 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli, Endoplasmic reticulum, Primary cilium; 额外: Microtu; UniProt: Endoplasmic reticulum membrane; Mitochondrion membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 373 aa / 42.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=416 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=94.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002225, IPR050177, IPR036291; Pfam: PF01073 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Endoplasmic reticulum, Primary cilium; 额外: Microtubules, Cytokinetic bridge, Primary cilium transition zone | Approved |
| UniProt | Endoplasmic reticulum membrane; Mitochondrion membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- ciliary transition zone (GO:0035869)
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- intercellular bridge (GO:0045171)
- microtubule cytoskeleton (GO:0015630)
- mitochondrial inner membrane (GO:0005743)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 416 |
| PubMed broad count | 651 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: 3BH, HSDB3A |

**关键文献**:
1. Spatial transcriptomics reveals altered lipid metabolism and inflammation-related gene expression of sebaceous glands in psoriasis and atopic dermatitis.. *Frontiers in immunology*. PMID: 38433843
2. Expression and gene variation studies deny association of human HSD3B1 gene with aldosterone production or blood pressure.. *American journal of hypertension*. PMID: 24951726
3. Germline HSD3B1 Genetics and Prostate Cancer Outcomes.. *Urology*. PMID: 32866512
4. HSD3B1 Genotypes Conferring Adrenal-Restrictive and Adrenal-Permissive Phenotypes in Prostate Cancer and Beyond.. *Endocrinology*. PMID: 31271415
5. HSD3B1 variant and androgen-deprivation therapy outcome in prostate cancer.. *Cancer chemotherapy and pharmacology*. PMID: 33141329

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.2 |
| 高置信度残基 (pLDDT>90) 占比 | 86.3% |
| 置信残基 (pLDDT 70-90) 占比 | 12.9% |
| 中等置信 (pLDDT 50-70) 占比 | 0.5% |
| 低置信 (pLDDT<50) 占比 | 0.3% |
| 有序区域 (pLDDT>70) 占比 | 99.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.2，有序区 99.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002225, IPR050177, IPR036291; Pfam: PF01073 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CYP11A1 | 0.997 | 0.108 | — |
| CYP17A1 | 0.995 | 0.108 | — |
| CYP19A1 | 0.988 | 0.108 | — |
| CYP11B1 | 0.984 | 0.108 | — |
| HSD17B3 | 0.983 | 0.000 | — |
| CYP21A2 | 0.979 | 0.108 | — |
| CYP11B2 | 0.979 | 0.108 | — |
| SRD5A1 | 0.971 | 0.000 | — |
| AKR1C3 | 0.971 | 0.000 | — |
| CYP7B1 | 0.970 | 0.310 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UGGT1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TMEM14B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| AQP6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SLC16A13 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| HSD3B2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GSN | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| FGFR3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| DLST | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| CALR | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.2 + PDB: 无 | pLDDT=94.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Mitochondrion memb / Nucleoli, Endoplasmic reticulum, Primary cilium; 额 | 一致 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. HSD3B1 — 3 beta-hydroxysteroid dehydrogenase/Delta 5-->4-isomerase type 1，研究基础较多，新颖性有限。
2. 蛋白大小373 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 416 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 416 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P14060
- Protein Atlas: https://www.proteinatlas.org/ENSG00000203857-HSD3B1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HSD3B1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P14060
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
