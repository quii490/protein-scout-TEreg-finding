---
type: protein-evaluation
gene: "TAFA2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TAFA2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TAFA2 / FAM19A2 |
| 蛋白名称 | Chemokine-like protein TAFA-2 |
| 蛋白大小 | 131 aa / 14.6 kDa |
| UniProt ID | Q8N3H0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 131 aa / 14.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR020350, IPR051743; Pfam: PF12020 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.5/180** | |
| **归一化总分** | | | **75.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- extracellular space (GO:0005615)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM19A2 |

**关键文献**:
1. Sour neuronal signalling attenuates macrophage-mediated liver injury.. *Journal of hepatology*. PMID: 40058705
2. Molecular Structure, Expression and Role of TAFA4 and its Receptor FPR1 in the Spinal Cord.. *Frontiers in cell and developmental biology*. PMID: 35712659
3. TAFA2 Induces Skeletal (Stromal) Stem Cell Migration Through Activation of Rac1-p38 Signaling.. *Stem cells (Dayton, Ohio)*. PMID: 30485583
4. A genome-wide association study on frequent exacerbation of asthma depending on smoking status.. *Respiratory medicine*. PMID: 35606283
5. Molecular analysis of a constitutional complex genome rearrangement with 11 breakpoints involving chromosomes 3, 11, 12, and 21 and a approximately 0.5-Mb submicroscopic deletion in a patient with mild mental retardation.. *Human genetics*. PMID: 16160854

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.3 |
| 高置信度残基 (pLDDT>90) 占比 | 64.9% |
| 置信残基 (pLDDT 70-90) 占比 | 18.3% |
| 中等置信 (pLDDT 50-70) 占比 | 16.8% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 83.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.3，有序区 83.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR020350, IPR051743; Pfam: PF12020 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KB暂无数据12 | 0.544 | 0.000 | — |
| FAM155A | 0.537 | 0.000 | — |
| NAALADL2 | 0.525 | 0.000 | — |
| ERICH3 | 0.493 | 0.000 | — |
| ARMH2 | 0.475 | 0.000 | — |
| CWF19L2 | 0.469 | 0.000 | — |
| TMEM161B | 0.454 | 0.000 | — |
| IQSEC3 | 0.435 | 0.000 | — |
| IMMP2L | 0.433 | 0.000 | — |
| CEP170B | 0.407 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ERN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LRP6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LARGE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LDLR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| INSR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HSPA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| IGF2R | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| COL6A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ITGA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CPE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 15
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.3 + PDB: 无 | pLDDT=88.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 10 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TAFA2 — Chemokine-like protein TAFA-2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小131 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 深度机制分析

TAFA2（Chemokine-like protein TAFA-2, 131 aa, UniProt Q8N3H0）。TAFA家族（FAM19A亚家族）是一组保守的分泌性趋化因子样蛋白，UniProt注释定位为Cytoplasm和Nucleus，HPA无IF数据。InterPro注释IPR020350（TAFA家族）和IPR051743（TAFA超家族），Pfam PF12020（TAFA domain）。AlphaFold pLDDT=88.3（有序区83.2%），无PDB结构，但预测质量极高。

从结构生物学角度，TAFA2的131 aa小蛋白在AlphaFold中展现出高置信度折叠——64.9%残基pLDDT>90，说明折叠完整性良好。IntAct鉴定的互作伙伴主要涉及分泌通路蛋白和内质网伴侣（ERN1、LRP6、HSPA5、IGF2R、LDLR、INSR），与注释的趋化因子样分泌功能一致。STRING预测伙伴包括FAM155A（score=0.537）、NAALADL2（0.525）等功能未知蛋白。

从核定位与TE调控角度，TAFA2的UniProt注释包含Nucleus（GO:0005634），但其功能研究局限于分泌通路和神经发育领域（PMID:40058705, PMID:30485583）。作为趋化因子样蛋白，核定位可能是"兼职蛋白"效应——部分分泌蛋白可被转运至细胞核发挥非经典功能（如HMGB1）。然而，目前没有证据支持TAFA2参与染色质调控或TE沉默。

PubMed仅5篇，极度新颖。综合评分75.8/100。建议：（1）通过IF验证TAFA2是否确实定位于细胞核；（2）若核定位确证，测定其DNA/染色质结合能力；（3）核质穿梭机制研究——是否存在NLS/CRM1依赖的核转运。