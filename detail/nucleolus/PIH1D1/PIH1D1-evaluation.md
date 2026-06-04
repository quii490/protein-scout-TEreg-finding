---
type: protein-evaluation
gene: "PIH1D1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PIH1D1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PIH1D1 / NOP17 |
| 蛋白名称 | PIH1 domain-containing protein 1 |
| 蛋白大小 | 290 aa / 32.4 kDa |
| UniProt ID | Q9NWS0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 290 aa / 32.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=78.8; PDB: 4PSF, 4PSI, 6GXZ, 7AVC, 8BDU |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050734, IPR012981, IPR041442; Pfam: PF08190, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleolus (GO:0005730)
- nucleus (GO:0005634)
- pre-snoRNP complex (GO:0070761)
- R2TP complex (GO:0097255)
- ribonucleoprotein complex (GO:1990904)
- RPAP3/R2TP/prefoldin-like complex (GO:1990062)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 42 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NOP17 |

**关键文献**:
1. The HSP90/R2TP Quaternary Chaperone Scaffolds Assembly of the TSC Complex.. *Journal of molecular biology*. PMID: 39490680
2. MRE11 stability is regulated by CK2-dependent interaction with R2TP complex.. *Oncogene*. PMID: 28436950
3. PIH1D1 and RPAP3, Components of the PAQosome: Emerging Roles in Cellular Physiology.. *Molecular and cellular biology*. PMID: 41424038
4. Structure of the Human TELO2-TTI1-TTI2 Complex.. *Journal of molecular biology*. PMID: 34838521
5. PIH1D1, a subunit of R2TP complex, inhibits doxorubicin-induced apoptosis.. *Biochemical and biophysical research communications*. PMID: 21078300

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.8 |
| 高置信度残基 (pLDDT>90) 占比 | 32.4% |
| 置信残基 (pLDDT 70-90) 占比 | 46.2% |
| 中等置信 (pLDDT 50-70) 占比 | 8.6% |
| 低置信 (pLDDT<50) 占比 | 12.8% |
| 有序区域 (pLDDT>70) 占比 | 78.6% |
| 可用 PDB 条目 | 4PSF, 4PSI, 6GXZ, 7AVC, 8BDU |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（4PSF, 4PSI, 6GXZ, 7AVC, 8BDU）+ AlphaFold极高置信度预测（pLDDT=78.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050734, IPR012981, IPR041442; Pfam: PF08190, PF18201 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RPAP3 | 0.999 | 0.992 | — |
| RUVBL2 | 0.999 | 0.966 | — |
| RUVBL1 | 0.999 | 0.974 | — |
| NOP58 | 0.994 | 0.856 | — |
| WDR92 | 0.990 | 0.855 | — |
| HSP90AA1 | 0.987 | 0.441 | — |
| POLR2E | 0.977 | 0.835 | — |
| UXT | 0.976 | 0.837 | — |
| PDRG1 | 0.976 | 0.815 | — |
| HSP90AB1 | 0.972 | 0.249 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| enok | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| Cdc45 | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| "fs | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG12256 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| GCC88 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG10710 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Exn | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG4286 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Drep2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| flw | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.8 + PDB: 4PSF, 4PSI, 6GXZ, 7AVC, 8BDU | pLDDT=78.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Cytosol | 一致 |
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
1. PIH1D1 — PIH1 domain-containing protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小290 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NWS0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104872-PIH1D1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PIH1D1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NWS0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
