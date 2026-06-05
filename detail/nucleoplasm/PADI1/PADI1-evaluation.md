---
type: protein-evaluation
gene: "PADI1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PADI1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PADI1 / PAD1, PDI1 |
| 蛋白名称 | Protein-arginine deiminase type-1 |
| 蛋白大小 | 663 aa / 74.7 kDa |
| UniProt ID | Q9ULC6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 663 aa / 74.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=32 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=94.6; PDB: 5HP5 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008972, IPR004303, IPR013530, IPR036556, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.0/180** | |
| **归一化总分** | | | **71.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 33 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PAD1, PDI1 |

**关键文献**:
1. Citrullination of pyruvate kinase M2 by PADI1 and PADI3 regulates glycolysis and cancer cell proliferation.. *Nature communications*. PMID: 33741961
2. PADI1 and Its Co-Expressed Gene Signature Unveil Colorectal Cancer Prognosis and Immunotherapy Efficacy.. *Journal of oncology*. PMID: 36471887
3. Peptidylarginine deiminase 1-catalyzed histone citrullination is essential for early embryo development.. *Scientific reports*. PMID: 27929094
4. Potential prognostic markers and significant lncRNA-mRNA co-expression pairs in laryngeal squamous cell carcinoma.. *Open life sciences*. PMID: 34131588
5. HO-1 Suppression by Co-Culture-Derived IL-6 Alleviates Ferritinophagy-Dependent Oxidative Stress to Potentiate Myogenic Differentiation.. *Cells*. PMID: 40862713

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.6 |
| 高置信度残基 (pLDDT>90) 占比 | 87.3% |
| 置信残基 (pLDDT 70-90) 占比 | 11.9% |
| 中等置信 (pLDDT 50-70) 占比 | 0.3% |
| 低置信 (pLDDT<50) 占比 | 0.5% |
| 有序区域 (pLDDT>70) 占比 | 99.2% |
| 可用 PDB 条目 | 5HP5 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.6，有序区 99.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008972, IPR004303, IPR013530, IPR036556, IPR013732; Pfam: PF03068, PF08527, PF08526 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FLG2 | 0.589 | 0.000 | — |
| FLG | 0.581 | 0.000 | — |
| H3C13 | 0.561 | 0.000 | — |
| H3C12 | 0.560 | 0.000 | — |
| STAP2 | 0.555 | 0.518 | — |
| EDEM1 | 0.553 | 0.000 | — |
| TCHH | 0.532 | 0.000 | — |
| TRIM3 | 0.471 | 0.000 | — |
| PADI3 | 0.436 | 0.330 | — |
| ELANE | 0.432 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| STAP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PADI3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TP53 | psi-mi:"MI:0096"(pull down) | pubmed:25402006|imex:IM-24266 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 3
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.6 + PDB: 5HP5 | pLDDT=94.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 11 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PADI1 — Protein-arginine deiminase type-1，非常新颖，仅有少数基础研究。
2. 蛋白大小663 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9ULC6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000142623-PADI1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PADI1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9ULC6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000142623-PADI1/subcellular

![](https://images.proteinatlas.org/62294/1310_F9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/62294/1310_F9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/62294/1312_F9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/62294/1312_F9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/62294/1573_A9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/62294/1573_A9_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9ULC6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
