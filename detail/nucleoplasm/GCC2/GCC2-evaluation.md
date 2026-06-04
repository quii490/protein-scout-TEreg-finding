---
type: protein-evaluation
gene: "GCC2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GCC2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GCC2 / KIAA0336, RANBP2L4 |
| 蛋白名称 | GRIP and coiled-coil domain-containing protein 2 |
| 蛋白大小 | 1684 aa / 195.9 kDa |
| UniProt ID | Q8IWJ2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; 额外: Nucleoplasm; UniProt: Cytoplasm; Golgi apparatus, trans-Golgi network membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 1684 aa / 195.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=71.7; PDB: 3BBP |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR032023, IPR000237, IPR051841; Pfam: PF01465, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **122.0/180** | |
| **归一化总分** | | | **67.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm | Enhanced |
| UniProt | Cytoplasm; Golgi apparatus, trans-Golgi network membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- trans-Golgi network (GO:0005802)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 62 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0336, RANBP2L4 |

**关键文献**:
1. RANBP2 evolution and human disease.. *FEBS letters*. PMID: 37795679
2. The Golgi complex governs natural killer cell lytic granule positioning to promote directionality in cytotoxicity.. *Cell reports*. PMID: 39813120
3. Golgi-endosome transport mediated by M6PR facilitates release of antisense oligonucleotides from endosomes.. *Nucleic acids research*. PMID: 31840180
4. Multiscale genetic architecture of donor-recipient differences reveals intronic LIMS1 mismatches associated with kidney transplant survival.. *The Journal of clinical investigation*. PMID: 37676733
5. Interruption of post-Golgi STING trafficking activates tonic interferon signaling.. *Nature communications*. PMID: 36379959

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.7 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 73.5% |
| 中等置信 (pLDDT 50-70) 占比 | 13.0% |
| 低置信 (pLDDT<50) 占比 | 13.5% |
| 有序区域 (pLDDT>70) 占比 | 73.5% |
| 可用 PDB 条目 | 3BBP |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=71.7，有序区 73.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032023, IPR000237, IPR051841; Pfam: PF01465, PF16704 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAB6A | 0.999 | 0.982 | — |
| STX16 | 0.978 | 0.000 | — |
| RAB9A | 0.976 | 0.073 | — |
| STX10 | 0.966 | 0.000 | — |
| GRIP1 | 0.959 | 0.000 | — |
| CLASRP | 0.954 | 0.000 | — |
| RANBP2 | 0.946 | 0.071 | — |
| GOLGA4 | 0.939 | 0.000 | — |
| RAB9B | 0.926 | 0.000 | — |
| RAB6B | 0.883 | 0.492 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-28984280 | psi-mi:"MI:0071"(molecular sieving) | imex:IM-12024|pubmed:18243103 |
| Wasf2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| EBI-1388758 | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-12024|pubmed:18243103 |
| RAB6A | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-12024|pubmed:18243103 |
| RAB9A | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-12024|pubmed:18243103 |
| 24451" | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-12024|pubmed:18243103 |
| ARL1 | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-12024|pubmed:18243103 |
| ZRANB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| ESR2 | psi-mi:"MI:0029"(cosedimentation through density g | imex:IM-13781|pubmed:21182203 |
| Q74YL2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.7 + PDB: 3BBP | pLDDT=71.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Golgi apparatus, trans-Golgi network me / Golgi apparatus; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GCC2 — GRIP and coiled-coil domain-containing protein 2，非常新颖，仅有少数基础研究。
2. 蛋白大小1684 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IWJ2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135968-GCC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GCC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IWJ2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
