---
type: protein-evaluation
gene: "AGO3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## AGO3 — REJECTED (研究热度过高 (PubMed strict=139，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AGO3 / EIF2C3 |
| 蛋白名称 | Protein argonaute-3 |
| 蛋白大小 | 860 aa / 97.4 kDa |
| UniProt ID | Q9H9G7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytoplasmic bodies; 额外: Nucleoplasm, Cytosol; UniProt: Cytoplasm, P-body |
| 蛋白大小 | 8/10 | ×1 | 8 | 860 aa / 97.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=139 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=91.5; PDB: 5VM9, 8VAJ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR028603, IPR014811, IPR032472, IPR032473, IPR032 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytoplasmic bodies; 额外: Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm, P-body | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- condensed nuclear chromosome (GO:0000794)
- cytoplasm (GO:0005737)
- cytoplasmic ribonucleoprotein granule (GO:0036464)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- P-body (GO:0000932)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 139 |
| PubMed broad count | 234 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EIF2C3 |

**关键文献**:
1. tRNA-derived small RNA, 5'tiRNA-Gly-CCC, promotes skeletal muscle regeneration through the inflammatory response.. *Journal of cachexia, sarcopenia and muscle*. PMID: 36755335
2. Human Argonaute3 has slicer activity.. *Nucleic acids research*. PMID: 29040713
3. Anatomy of four human Argonaute proteins.. *Nucleic acids research*. PMID: 35736234
4. Burden re-analysis of neurodevelopmental disorder cohorts for prioritization of candidate genes.. *European journal of human genetics : EJHG*. PMID: 38965372
5. AGO3 Slicer activity regulates mitochondria-nuage localization of Armitage and piRNA amplification.. *The Journal of cell biology*. PMID: 25049272

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.5 |
| 高置信度残基 (pLDDT>90) 占比 | 81.5% |
| 置信残基 (pLDDT 70-90) 占比 | 12.9% |
| 中等置信 (pLDDT 50-70) 占比 | 2.1% |
| 低置信 (pLDDT<50) 占比 | 3.5% |
| 有序区域 (pLDDT>70) 占比 | 94.4% |
| 可用 PDB 条目 | 5VM9, 8VAJ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（5VM9, 8VAJ）+ AlphaFold高质量预测（pLDDT=91.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028603, IPR014811, IPR032472, IPR032473, IPR032474; Pfam: PF08699, PF16488, PF16487 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AGO2 | 0.997 | 0.837 | — |
| DICER1 | 0.991 | 0.865 | — |
| AGO1 | 0.988 | 0.720 | — |
| TNRC6A | 0.987 | 0.843 | — |
| TNRC6C | 0.972 | 0.889 | — |
| TNRC6B | 0.968 | 0.833 | — |
| TARBP2 | 0.968 | 0.606 | — |
| AGO4 | 0.966 | 0.627 | — |
| DROSHA | 0.947 | 0.405 | — |
| DDX6 | 0.926 | 0.387 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.5 + PDB: 5VM9, 8VAJ | pLDDT=91.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, P-body / Cytoplasmic bodies; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. AGO3 — Protein argonaute-3，研究基础较多，新颖性有限。
2. 蛋白大小860 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 139 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 139 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H9G7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000126070-AGO3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AGO3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H9G7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
