---
type: protein-evaluation
gene: "HSD17B6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HSD17B6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HSD17B6 / RODH, SDR9C6 |
| 蛋白名称 | 17-beta-hydroxysteroid dehydrogenase type 6 |
| 蛋白大小 | 317 aa / 36.0 kDa |
| UniProt ID | O14756 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; UniProt: Microsome membrane; Early endosome membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 317 aa / 36.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=36 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=95.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036291, IPR020904, IPR002347; Pfam: PF00106 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | Microsome membrane; Early endosome membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- early endosome membrane (GO:0031901)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 36 |
| PubMed broad count | 93 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RODH, SDR9C6 |

**关键文献**:
1. Polymorphisms of the HSD17B6 and HSD17B5 genes in Chinese women with polycystic ovary syndrome.. *Journal of women's health (2002)*. PMID: 21039282
2. Downexpression of HSD17B6 correlates with clinical prognosis and tumor immune infiltrates in hepatocellular carcinoma.. *Cancer cell international*. PMID: 32514254
3. Hydroxysteroid 17-Beta Dehydrogenase 6 Is a Prognostic Biomarker and Correlates with Immune Infiltrates in Hepatocellular Carcinoma.. *Digestive diseases and sciences*. PMID: 33495920
4. GATA1 activates HSD17B6 to improve efficiency of cisplatin in lung adenocarcinoma via DNA damage.. *Genes and environment : the official journal of the Japanese Environmental Mutagen Society*. PMID: 39695810
5. HSD17B6 downregulation predicts poor prognosis and drives tumor progression via activating Akt signaling pathway in lung adenocarcinoma.. *Cell death discovery*. PMID: 34750355

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.9 |
| 高置信度残基 (pLDDT>90) 占比 | 93.4% |
| 置信残基 (pLDDT 70-90) 占比 | 6.6% |
| 中等置信 (pLDDT 50-70) 占比 | 0.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 100.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=95.9，有序区 100.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036291, IPR020904, IPR002347; Pfam: PF00106 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AKR1C3 | 0.978 | 0.000 | — |
| SRD5A1 | 0.976 | 0.000 | — |
| CYP17A1 | 0.970 | 0.045 | — |
| HSD17B3 | 0.954 | 0.000 | — |
| SRD5A2 | 0.953 | 0.000 | — |
| HSD3B2 | 0.952 | 0.000 | — |
| HSD3B1 | 0.952 | 0.000 | — |
| DHRS11 | 0.946 | 0.000 | — |
| SRD5A3 | 0.939 | 0.000 | — |
| HSD17B1 | 0.938 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ATP2B2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NME2P1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SNX3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATP2B1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATP2B4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATP12A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATP2B3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TATDN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPP1R14B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GNPNAT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.9 + PDB: 无 | pLDDT=95.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Microsome membrane; Early endosome membrane / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. HSD17B6 — 17-beta-hydroxysteroid dehydrogenase type 6，非常新颖，仅有少数基础研究。
2. 蛋白大小317 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 36 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14756
- Protein Atlas: https://www.proteinatlas.org/ENSG00000025423-HSD17B6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HSD17B6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14756
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
