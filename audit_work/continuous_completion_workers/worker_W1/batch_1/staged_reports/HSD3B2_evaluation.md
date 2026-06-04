---
type: protein-evaluation
gene: "HSD3B2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HSD3B2 — REJECTED (研究热度过高 (PubMed strict=256，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HSD3B2 / HSDB3B |
| 蛋白名称 | 3 beta-hydroxysteroid dehydrogenase/Delta 5-->4-isomerase type 2 |
| 蛋白大小 | 372 aa / 42.1 kDa |
| UniProt ID | P26439 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Endoplasmic reticulum, Primary cilium; 额外: Nucleoli, Microtu; UniProt: Endoplasmic reticulum membrane; Mitochondrion membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 372 aa / 42.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=256 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=94.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002225, IPR050177, IPR036291; Pfam: PF01073 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum, Primary cilium; 额外: Nucleoli, Microtubules, Cytokinetic bridge, Primary cilium transition zone | Approved |
| UniProt | Endoplasmic reticulum membrane; Mitochondrion membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（批量模式），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- ciliary transition zone (GO:0035869)
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- intercellular bridge (GO:0045171)
- membrane (GO:0016020)
- microtubule cytoskeleton (GO:0015630)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 256 |
| PubMed broad count | 355 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HSDB3B |

**关键文献**:
1. Mutation of HSD3B2 Gene and Fate of Dehydroepiandrosterone.. *Vitamins and hormones*. PMID: 30029738
2. Targeted Mutational Analysis of Cortisol-Producing Adenomas.. *The Journal of clinical endocrinology and metabolism*. PMID: 34534321
3. Hormonal carcinogenesis.. *Carcinogenesis*. PMID: 10688862
4. Immunohistochemical expression of CYP11A1, CYP11B, CYP17, and HSD3B2 in functional and nonfunctional canine adrenocortical tumors.. *Journal of veterinary internal medicine*. PMID: 39387578
5. Androgen production, uptake, and conversion (APUC) genes define prostate cancer patients with distinct clinical outcomes.. *JCI insight*. PMID: 39207857

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.4 |
| 高置信度残基 (pLDDT>90) 占比 | 85.5% |
| 置信残基 (pLDDT 70-90) 占比 | 13.7% |
| 中等置信 (pLDDT 50-70) 占比 | 0.8% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.4，有序区 99.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002225, IPR050177, IPR036291; Pfam: PF01073 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CYP17A1 | 0.994 | 0.108 | — |
| CYP11A1 | 0.994 | 0.108 | — |
| CYP11B1 | 0.992 | 0.108 | — |
| HSD17B3 | 0.987 | 0.000 | — |
| CYP21A2 | 0.985 | 0.108 | — |
| CYP11B2 | 0.984 | 0.108 | — |
| AKR1C3 | 0.981 | 0.000 | — |
| SRD5A1 | 0.980 | 0.000 | — |
| CYP19A1 | 0.979 | 0.108 | — |
| CYP7A1 | 0.972 | 0.310 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NARS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MACROH2A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LETM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| H2AC11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TOP2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSD3B1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TCEA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MTHFR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TOP2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.4 + PDB: 无 | pLDDT=94.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Mitochondrion memb / Endoplasmic reticulum, Primary cilium; 额外: Nucleol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. HSD3B2 — 3 beta-hydroxysteroid dehydrogenase/Delta 5-->4-isomerase type 2，研究基础较多，新颖性有限。
2. 蛋白大小372 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 256 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 256 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P26439
- Protein Atlas: https://www.proteinatlas.org/ENSG00000203859-HSD3B2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HSD3B2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P26439
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
