---
type: protein-evaluation
gene: "FBXO45"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXO45 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO45 / FBX45 |
| 蛋白名称 | F-box/SPRY domain-containing protein 1 |
| 蛋白大小 | 286 aa / 30.6 kDa |
| UniProt ID | P0C2W1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Plasma membrane, Cytosol; 额外: Vesicles; UniProt: Secreted; Postsynaptic cell membrane; Presynaptic cell membr |
| 蛋白大小 | 10/10 | ×1 | 10 | 286 aa / 30.6 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=60 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001870, IPR043136, IPR013320, IPR036047, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane, Cytosol; 额外: Vesicles | Approved |
| UniProt | Secreted; Postsynaptic cell membrane; Presynaptic cell membrane; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular region (GO:0005576)
- glutamatergic synapse (GO:0098978)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)
- postsynaptic cytosol (GO:0099524)
- postsynaptic density (GO:0014069)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 60 |
| PubMed broad count | 75 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBX45 |

**关键文献**:
1. FBXO45 is a potential therapeutic target for cancer therapy.. *Cell death discovery*. PMID: 32655893
2. Fbxo45 facilitates pancreatic carcinoma progression by targeting USP49 for ubiquitination and degradation.. *Cell death & disease*. PMID: 35279684
3. Elevated FBXO45 promotes TFG ubiquitination and drives lung metastasis of hepatocellular carcinoma.. *JHEP reports : innovation in hepatology*. PMID: 41030651
4. SETD7 drives diabetic endothelial dysfunction through FBXO45-mediated GPX4 ubiquitylation.. *Cardiovascular diabetology*. PMID: 40275362
5. Elevated FBXO45 promotes liver tumorigenesis through enhancing IGF2BP1 ubiquitination and subsequent PLK1 upregulation.. *eLife*. PMID: 34779401

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.7 |
| 高置信度残基 (pLDDT>90) 占比 | 81.8% |
| 置信残基 (pLDDT 70-90) 占比 | 4.2% |
| 中等置信 (pLDDT 50-70) 占比 | 3.1% |
| 低置信 (pLDDT<50) 占比 | 10.8% |
| 有序区域 (pLDDT>70) 占比 | 86.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.7，有序区 86.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001870, IPR043136, IPR013320, IPR036047, IPR001810; Pfam: PF12937, PF00622 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MYCBP2 | 0.999 | 0.942 | — |
| SKP1 | 0.999 | 0.863 | — |
| CUL1 | 0.911 | 0.651 | — |
| UNC13A | 0.858 | 0.000 | — |
| SPRYD3 | 0.785 | 0.591 | — |
| SIAH1 | 0.756 | 0.000 | — |
| FBXW7 | 0.752 | 0.626 | — |
| WDR53 | 0.743 | 0.000 | — |
| MPP3 | 0.719 | 0.000 | — |
| DLG3 | 0.716 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| USP11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Mycbp2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| LGALS3BP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NEURL4 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| RFC4 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| GALC | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| GDF10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FBXW7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.7 + PDB: 无 | pLDDT=88.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Secreted; Postsynaptic cell membrane; Presynaptic  / Nucleoplasm, Plasma membrane, Cytosol; 额外: Vesicle | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. FBXO45 — F-box/SPRY domain-containing protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小286 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 60 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P0C2W1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174013-FBXO45/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO45
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P0C2W1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
