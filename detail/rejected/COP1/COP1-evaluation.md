---
type: protein-evaluation
gene: "COP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## COP1 — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3); 研究热度过高 (PubMed strict=672，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COP1 / COP, COP1 |
| 蛋白名称 | Caspase recruitment domain-containing protein 16 |
| 蛋白大小 | 197 aa / 22.6 kDa |
| UniProt ID | Q5EG05 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 197 aa / 22.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=672 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001315, IPR011029, IPR002398; Pfam: PF00619 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **61.5/180** | |
| **归一化总分** | | | **34.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- protease inhibitor complex (GO:0097179)
- protein-containing complex (GO:0032991)

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 672 |
| PubMed broad count | 1062 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: COP, COP1 |

**关键文献**:
1. COP1 and BBXs-HY5-mediated light signal transduction in plants.. *The New phytologist*. PMID: 31664720
2. In vivo CRISPR screens identify the E3 ligase Cop1 as a modulator of macrophage infiltration and cancer immunotherapy target.. *Cell*. PMID: 34582788
3. Ubiquitin Ligase COP1 Suppresses Neuroinflammation by Degrading c/EBPβ in Microglia.. *Cell*. PMID: 32795415
4. MET promotes hepatocellular carcinoma development through the promotion of TRIB3-mediated FOXO1 degradation.. *Clinical and molecular hepatology*. PMID: 40211872
5. CUL4B-DDB1-COP1-mediated UTX downregulation promotes colorectal cancer progression.. *Experimental hematology & oncology*. PMID: 37679762

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.0 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 44.7% |
| 中等置信 (pLDDT 50-70) 占比 | 31.0% |
| 低置信 (pLDDT<50) 占比 | 24.4% |
| 有序区域 (pLDDT>70) 占比 | 44.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=65.0），有序残基占 44.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001315, IPR011029, IPR002398; Pfam: PF00619 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DET1 | 0.997 | 0.873 | — |
| DDB1 | 0.995 | 0.854 | — |
| CUL4A | 0.993 | 0.787 | — |
| RBX1 | 0.987 | 0.608 | — |
| CUL4B | 0.966 | 0.620 | — |
| TP53 | 0.961 | 0.833 | — |
| DDA1 | 0.960 | 0.619 | — |
| DDB2 | 0.951 | 0.201 | — |
| CDKN1B | 0.928 | 0.292 | — |
| DCAF11 | 0.919 | 0.229 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q1JPL6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:18812498|imex:IM-20112 |
| SPA3 | psi-mi:"MI:0018"(two hybrid) | pubmed:12887588 |
| SPA4 | psi-mi:"MI:0018"(two hybrid) | pubmed:12887588 |
| SPA1 | psi-mi:"MI:0018"(two hybrid) | pubmed:11461903 |
| CSN3 | psi-mi:"MI:0071"(molecular sieving) | pubmed:14597662|mint:MINT-5216 |
| CSN6A | psi-mi:"MI:0071"(molecular sieving) | pubmed:14597662|mint:MINT-5216 |
| CIP8 | psi-mi:"MI:0096"(pull down) | pubmed:12028569 |
| COP10 | psi-mi:"MI:0018"(two hybrid) | pubmed:16844902|imex:IM-20340 |
| CUL4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16844902|imex:IM-20340 |
| COL1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:18812498|imex:IM-20112 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.0 + PDB: 无 | pLDDT=65.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. COP1 — Caspase recruitment domain-containing protein 16，研究基础较多，新颖性有限。
2. 蛋白大小197 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 672 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=65.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5EG05
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143207-COP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5EG05
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
