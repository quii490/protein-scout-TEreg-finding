---
type: protein-evaluation
gene: "MSX1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MSX1 — REJECTED (研究热度过高 (PubMed strict=863，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MSX1 / HOX7 |
| 蛋白名称 | Homeobox protein MSX-1 |
| 蛋白大小 | 303 aa / 31.5 kDa |
| UniProt ID | P28360 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 303 aa / 31.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=863 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR020479, IPR017970, IPR009057, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nuclear periphery (GO:0034399)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 863 |
| PubMed broad count | 1311 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HOX7 |

**关键文献**:
1. PRMT1-methylated MSX1 phase separates to control palate development.. *Nature communications*. PMID: 39843447
2. MSX1 gene polymorphisms and non-syndromic cleft lip with or without palate (NSCL/P): A meta-analysis.. *Oral diseases*. PMID: 31132300
3. Association between PAX9 or MSX1 gene polymorphism and tooth agenesis risk: A meta-analysis.. *Open life sciences*. PMID: 40226363
4. Association of MSX1 Gene Variants with Nonsyndromic Cleft Lip and/or Palate in the Pakistani Population.. *The Cleft palate-craniofacial journal : official publication of the American Cleft Palate-Craniofacial Association*. PMID: 37431261
5. MSX1 gene polymorphisms in non-syndromic cleft lip and/or palate.. *Oral diseases*. PMID: 23130753

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.2 |
| 高置信度残基 (pLDDT>90) 占比 | 19.8% |
| 置信残基 (pLDDT 70-90) 占比 | 7.9% |
| 中等置信 (pLDDT 50-70) 占比 | 44.9% |
| 低置信 (pLDDT<50) 占比 | 27.4% |
| 有序区域 (pLDDT>70) 占比 | 27.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.2），有序残基占 27.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR020479, IPR017970, IPR009057, IPR050674; Pfam: PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| H1-5 | 0.985 | 0.078 | — |
| PAX9 | 0.983 | 0.095 | — |
| MSX2 | 0.957 | 0.292 | — |
| BMP4 | 0.910 | 0.000 | — |
| OSR2 | 0.873 | 0.095 | — |
| LHX8 | 0.853 | 0.071 | — |
| CSRNP1 | 0.845 | 0.000 | — |
| TGFB3 | 0.834 | 0.000 | — |
| LEF1 | 0.829 | 0.000 | — |
| IRF6 | 0.817 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| H1-5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15192231|imex:IM-19849 |
| MED19 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ING4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| NMNAT1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Maged1 | psi-mi:"MI:0096"(pull down) | pubmed:15272023|imex:IM-20069 |
| ENSMUSP00000058354.10 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15272023|imex:IM-20069 |
| Ndn | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15272023|imex:IM-20069 |
| RBPMS | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GMNN | psi-mi:"MI:0077"(nuclear magnetic resonance) | pubmed:22615398|imex:IM-27180 |
| TLE2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.2 + PDB: 无 | pLDDT=64.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. MSX1 — Homeobox protein MSX-1，研究基础较多，新颖性有限。
2. 蛋白大小303 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 863 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=64.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 863 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P28360
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163132-MSX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MSX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P28360
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
