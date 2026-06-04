---
type: protein-evaluation
gene: "NPLOC4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NPLOC4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NPLOC4 / KIAA1499, NPL4 |
| 蛋白名称 | Nuclear protein localization protein 4 homolog |
| 蛋白大小 | 608 aa / 68.1 kDa |
| UniProt ID | Q8TAT6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm, cytosol; Endoplasmic reticulum; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 608 aa / 68.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=28 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=87.6; PDB: 7WWP, 7WWQ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR037518, IPR016563, IPR007717, IPR024682, IPR007 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.0/180** | |
| **归一化总分** | | | **73.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm, cytosol; Endoplasmic reticulum; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- nuclear outer membrane-endoplasmic reticulum membrane network (GO:0042175)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- UFD1-NPL4 complex (GO:0036501)
- VCP-NPL4-UFD1 AAA ATPase complex (GO:0034098)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 79 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1499, NPL4 |

**关键文献**:
1. Copper metabolism in cell death and autophagy.. *Autophagy*. PMID: 37055935
2. VCP/p97 UFMylation stabilizes BECN1 and facilitates the initiation of autophagy.. *Autophagy*. PMID: 38762759
3. VCP regulates early tau seed amplification via specific cofactors.. *Molecular neurodegeneration*. PMID: 39773263
4. NPLOC4 constructs tumor immunosuppressive microenvironment in pan-cancer and hepatocellular carcinoma.. *Current medicinal chemistry*. PMID: 40685720
5. A UBH-UBX module amplifies p97/VCP's unfolding power to facilitate protein extraction and degradation.. *Nature communications*. PMID: 41258083

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.6 |
| 高置信度残基 (pLDDT>90) 占比 | 65.8% |
| 置信残基 (pLDDT 70-90) 占比 | 25.7% |
| 中等置信 (pLDDT 50-70) 占比 | 2.6% |
| 低置信 (pLDDT<50) 占比 | 5.9% |
| 有序区域 (pLDDT>70) 占比 | 91.5% |
| 可用 PDB 条目 | 7WWP, 7WWQ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（7WWP, 7WWQ）+ AlphaFold高质量预测（pLDDT=87.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037518, IPR016563, IPR007717, IPR024682, IPR007716; Pfam: PF05021, PF11543, PF05020 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FAF1 | 0.999 | 0.996 | — |
| FAF2 | 0.999 | 0.996 | — |
| UFD1 | 0.999 | 0.999 | — |
| VCP | 0.999 | 0.999 | — |
| UBXN7 | 0.999 | 0.998 | — |
| VCPIP1 | 0.998 | 0.994 | — |
| UBC | 0.998 | 0.992 | — |
| ASPSCR1 | 0.997 | 0.994 | — |
| NSFL1C | 0.997 | 0.994 | — |
| UBXN10 | 0.995 | 0.994 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSRNOP00000068982.2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| FAF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| Nsfl1c | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| FAF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| UBXN7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| UBXN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| UBXN8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| Ubxn11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| UBXN10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| VCPIP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.6 + PDB: 7WWP, 7WWQ | pLDDT=87.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Endoplasmic reticulum; Nucleus / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. NPLOC4 — Nuclear protein localization protein 4 homolog，非常新颖，仅有少数基础研究。
2. 蛋白大小608 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TAT6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182446-NPLOC4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NPLOC4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TAT6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
