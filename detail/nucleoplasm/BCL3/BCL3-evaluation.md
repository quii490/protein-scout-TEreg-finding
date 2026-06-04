---
type: protein-evaluation
gene: "BCL3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BCL3 — REJECTED (研究热度过高 (PubMed strict=485，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BCL3 / BCL4, D19S37 |
| 蛋白名称 | B-cell lymphoma 3 protein |
| 蛋白大小 | 454 aa / 47.6 kDa |
| UniProt ID | P20749 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles, Midbody, Primary cilium, Basal bo; UniProt: Nucleus; Cytoplasm; Cytoplasm, perinuclear region |
| 蛋白大小 | 10/10 | ×1 | 10 | 454 aa / 47.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=485 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=71.3; PDB: 1K1A, 1K1B |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770, IPR051070; Pfam: PF00023, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **90.0/180** | |
| **归一化总分** | | | **50.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Midbody, Primary cilium, Basal body, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Bcl3-Bcl10 complex (GO:0032996)
- Bcl3/NF-kappaB2 complex (GO:0033257)
- ciliary basal body (GO:0036064)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- midbody (GO:0030496)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 485 |
| PubMed broad count | 958 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BCL4, D19S37 |

**关键文献**:
1. IĸB Protein BCL3 as a Controller of Osteogenesis and Bone Health.. *Arthritis & rheumatology (Hoboken, N.J.)*. PMID: 37410754
2. Clinical and transcriptomic characterization of patients with chronic lymphocytic leukemia harboring t(14;19): an ERIC study.. *Leukemia*. PMID: 40973766
3. BCL3-PVRL2-TOMM40 SNPs, gene-gene and gene-environment interactions on dyslipidemia.. *Scientific reports*. PMID: 29670124
4. The atypical IκB family member Bcl3 determines differentiation and fate of intestinal RORγt(+) regulatory T-cell subsets.. *Mucosal immunology*. PMID: 38663461
5. Liver-specific Bcl3 Knockout Alleviates Acetaminophen-induced Liver Injury by Activating Nrf2 Pathway in Male Mice.. *Cellular and molecular gastroenterology and hepatology*. PMID: 40015625

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.3 |
| 高置信度残基 (pLDDT>90) 占比 | 49.3% |
| 置信残基 (pLDDT 70-90) 占比 | 3.5% |
| 中等置信 (pLDDT 50-70) 占比 | 8.1% |
| 低置信 (pLDDT<50) 占比 | 39.0% |
| 有序区域 (pLDDT>70) 占比 | 52.8% |
| 可用 PDB 条目 | 1K1A, 1K1B |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1K1A, 1K1B）+ AlphaFold高质量预测（pLDDT=71.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR051070; Pfam: PF00023, PF12796 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NFKB1 | 0.999 | 0.835 | — |
| NFKB2 | 0.999 | 0.784 | — |
| CYLD | 0.986 | 0.528 | — |
| PIR | 0.983 | 0.516 | — |
| RELB | 0.959 | 0.344 | — |
| REL | 0.952 | 0.188 | — |
| RELA | 0.951 | 0.188 | — |
| HDAC1 | 0.909 | 0.537 | — |
| NFKBIA | 0.904 | 0.000 | — |
| FOS | 0.856 | 0.300 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BCL10 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-14497|pubmed:16280327 |
| CTBP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15364|pubmed:21988832 |
| ANKRD28 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| HSPA6 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| NFKB1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| NFKB2 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| HSPH1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| NUP58 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| Cyld | psi-mi:"MI:0018"(two hybrid) | imex:IM-12034|pubmed:16713561 |
| - | psi-mi:"MI:0096"(pull down) | imex:IM-24619|pubmed:24634496 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.3 + PDB: 1K1A, 1K1B | pLDDT=71.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, perinuclear region / Nucleoplasm; 额外: Vesicles, Midbody, Primary cilium | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BCL3 — B-cell lymphoma 3 protein，研究基础较多，新颖性有限。
2. 蛋白大小454 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 485 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 485 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P20749
- Protein Atlas: https://www.proteinatlas.org/ENSG00000069399-BCL3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BCL3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P20749
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
