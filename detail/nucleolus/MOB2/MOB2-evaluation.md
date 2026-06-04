---
type: protein-evaluation
gene: "MOB2"
date: 2026-06-03
tags: [protein-scout, nucleolus, re-evaluation, recovery]
status: scored
category: nucleolus
normalized_score: 70.2
raw_score: 128.5
nuclear_score: 7
---

## MOB2 核蛋白评估报告 (Full Re-evaluation)


### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MOB2 / HCCA2 |
| 蛋白名称 | MOB kinase activator 2 |
| 蛋白大小 | 237 aa / 26.9 kDa |
| UniProt ID | Q70IA6 |
| PubMed (strict) | 34 |
| PubMed (broad) | 102 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; Nucleoplasm, Cytosol; UniProt: Nucleus; Cytoplasm, perinuclear region |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 237 aa / 26.9 kDa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=34 篇 (21-40→8) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.0，PDB: 无 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR005301, IPR036703; Pfam: PF03637 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners, IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/183** | |
| **归一化总分** | | | **70.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; Nucleoplasm, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持，部分数据源提示非核定位但核信号主导。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 102 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HCCA2 |

**关键文献**:
1. MOB2 suppresses GBM cell migration and invasion via regulation of FAK/Akt and cAMP/PKA signaling.. *Cell death & disease*. PMID: 32286266
2. Ndr/Lats Kinases Bind Specific Mob-Family Coactivators through a Conserved and Modular Interface.. *Biochemistry*. PMID: 32250593
3. The NDR kinase-MOB complex FgCot1-Mob2 regulates polarity and lipid metabolism in Fusarium graminearum.. *Environmental microbiology*. PMID: 34347361
4. Lre1 directly inhibits the NDR/Lats kinase Cbk1 at the cell division site in a phosphorylation-dependent manner.. *Current biology : CB*. PMID: 23954433
5. The promotion of neurite formation in Neuro2A cells by mouse Mob2 protein.. *FEBS letters*. PMID: 21237165

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.0 |
| 高置信度残基 (pLDDT>90) 占比 | 71.3% |
| 置信残基 (pLDDT 70-90) 占比 | 8.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.0% |
| 低置信 (pLDDT<50) 占比 | 17.7% |
| 有序区域 (pLDDT>70) 占比 | 79.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold 极高置信度预测（pLDDT=85.0，有序区 79.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005301, IPR036703; Pfam: PF03637 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| STK38L | 0.974 | 0.884 | — |
| STK38 | 0.971 | 0.822 | — |
| MOB4 | 0.786 | 0.000 | — |
| DIMT1 | 0.532 | 0.000 | — |
| NTSR1 | 0.506 | 0.000 | — |
| LATS1 | 0.500 | 0.069 | — |
| KRTAP5-1 | 0.477 | 0.000 | — |
| FRYL | 0.474 | 0.000 | — |
| STK24 | 0.462 | 0.070 | — |
| MAP2K7 | 0.462 | 0.355 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NAF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| CBK1 | psi-mi:"MI:0018"(two hybrid) | pubmed:12972564|imex:IM-19700 |
| SET3 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-14085|pubmed:21179020 |
| LGE1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-14085|pubmed:21179020 |
| CPR1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-14085|pubmed:21179020 |
| FPR2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-14085|pubmed:21179020 |
| BRE1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-14085|pubmed:21179020 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSE1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| CRM1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |

**已知复合体成员** (GO Cellular Component):
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.0 + PDB: 无 | pLDDT=85.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, perinuclear region / Nucleoli; Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MOB2 — MOB kinase activator 2，非常新颖，仅有少数基础研究。
2. 蛋白大小237 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q70IA6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182208-MOB2
- Protein Atlas Subcellular: https://www.proteinatlas.org/ENSG00000182208-MOB2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MOB2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q70IA6
- STRING: https://string-db.org/network
- IntAct: https://www.ebi.ac.uk/intact/search?query=MOB2
- Packet data timestamp: 2026-06-03 21:50:18

---

*本报告基于最新的 harvest packet 数据（2026-06-03 21:50:18），各数据库实时抓取。评分严格遵循 /180 加权评分体系：核定位×4 + 大小×1 + 新颖性×5 + 结构×3 + 结构域×2 + PPI×3 + 互证加分（max+3）。PubMed>100 或 核定位≤3 为 REJECTED。*
