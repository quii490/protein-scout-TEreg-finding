---
type: protein-evaluation
gene: "STRADA"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## STRADA 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STRADA / LYK5, STRAD |
| 蛋白名称 | STE20-related kinase adapter protein alpha |
| 蛋白大小 | 431 aa / 48.4 kDa |
| UniProt ID | Q7RTN6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 431 aa / 48.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=80.0; PDB: 1UPK, 2WTK, 3GNI, 8VSU |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011009, IPR000719, IPR047173; Pfam: PF00069 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **143.0/180** | |
| **归一化总分** | | | **79.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- intracellular protein-containing complex (GO:0140535)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- serine/threonine protein kinase complex (GO:1902554)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 7680 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LYK5, STRAD |

**关键文献**:
1. Electroclinical Features in Two Novel STRADA Patients and a Functional Yeast Assay for the Validation of Missense STRADA Mutations.. *Pediatric neurology*. PMID: 37722301
2. Sevoflurane Postconditioning Reduces Hypoxia-Reoxygenation Injury in H9C2 Embryonic Rat Cardiomyocytes and Targets the STRADA Gene by Upregulating microRNA-107.. *Medical science monitor : international medical journal of experimental and clinical research*. PMID: 32332694
3. STRADA-mutant human cortical organoids model megalencephaly and exhibit delayed neuronal differentiation.. *Developmental neurobiology*. PMID: 33619909
4. Rapamycin prevents seizures after depletion of STRADA in a rare neurodevelopmental disorder.. *Science translational medicine*. PMID: 23616120
5. Novel Homozygous Deletion in STRADA Gene Associated With Polyhydramnios, Megalencephaly, and Epilepsy in 2 Siblings: Implications for Diagnosis and Treatment.. *Journal of child neurology*. PMID: 30311510

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.0 |
| 高置信度残基 (pLDDT>90) 占比 | 63.3% |
| 置信残基 (pLDDT 70-90) 占比 | 10.7% |
| 中等置信 (pLDDT 50-70) 占比 | 4.2% |
| 低置信 (pLDDT<50) 占比 | 21.8% |
| 有序区域 (pLDDT>70) 占比 | 74.0% |
| 可用 PDB 条目 | 1UPK, 2WTK, 3GNI, 8VSU |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1UPK, 2WTK, 3GNI, 8VSU）+ AlphaFold高质量预测（pLDDT=80.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR000719, IPR047173; Pfam: PF00069 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CAB39 | 0.999 | 0.983 | — |
| STK11 | 0.999 | 0.991 | — |
| CAB39L | 0.996 | 0.804 | — |
| PRKAA1 | 0.915 | 0.101 | — |
| PRKAA2 | 0.914 | 0.101 | — |
| STRADB | 0.911 | 0.000 | — |
| SEC61G | 0.828 | 0.750 | — |
| SEC63 | 0.824 | 0.752 | — |
| GOLGA2 | 0.820 | 0.000 | — |
| SEC62 | 0.812 | 0.750 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| STK11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14676191 |
| Stk25 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15303|pubmed:21111240 |
| LBHD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| C5orf24 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PIP4K2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CAB39L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| CAB39 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BIRC6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PFDN6 | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.0 + PDB: 1UPK, 2WTK, 3GNI, 8VSU | pLDDT=80.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. STRADA — STE20-related kinase adapter protein alpha，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小431 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7RTN6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000266173-STRADA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STRADA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7RTN6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000266173-STRADA/subcellular

![](https://images.proteinatlas.org/31637/1125_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/31637/1125_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/31637/1177_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/31637/1177_G6_7_red_green.jpg)
![](https://images.proteinatlas.org/31637/332_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/31637/332_D2_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7RTN6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
