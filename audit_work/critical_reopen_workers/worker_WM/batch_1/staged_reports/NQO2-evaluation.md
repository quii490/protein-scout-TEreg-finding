---
type: protein-evaluation
gene: "NQO2"
date: 2026-06-02
tags: [protein-scout, critical-reopen, false-rejection-reevaluated, rejected-on-reeval]
status: reevaluated
reeval_result: REJECT_CONFIRMED
original_rejection: "核定位证据弱 (胞质为主) + PubMed 146 > 100 + 代谢酶非调控蛋白"
---

## NQO2 -- RE-EVALUATED: REJECT CONFIRMED (原始总分 75.0/180, 归一化 41.7/100)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NQO2 (NMOR2) |
| 蛋白名称 | Ribosyldihydronicotinamide dehydrogenase [quinone] (NRH:quinone oxidoreductase 2) |
| 蛋白大小 | 231 aa / 25.9 kDa |
| UniProt ID | P16083 |
| 核定位 (HPA IF) | Cytosol (主), Nucleoplasm (额外); Supported |
| 核定位 (UniProt) | Cytoplasm |
| 评估日期 | 2026-06-02 |
| 原始淘汰原因 | 胞质为主代谢酶 + PubMed 146 > 100 |

### 2. False Rejection Recheck

**原始淘汰判定**: 核定位得分 4/10 (胞质为主) + PubMed 146 > 100 + 代谢酶非调控蛋白

**Recheck 发现**:

1. **核定位确实薄弱**: HPA 标注 Cytosol 为主定位, Nucleoplasm 为附加定位 (additional location)。UniProt 仅标注 Cytoplasm。GO-CC 中 nucleoplasm 有 IDA:HPA 证据, 但与 cytosol (IDA:CAFA) 相比, 胞质定位的证据更直接。NQO2 主要作为胞质醌还原酶发挥作用, 核内分布可能是次要或被动扩散。

2. **研究热度远超阈值**: PubMed strict=146, symbol_only=246, broad=247。NQO2 作为醌还原酶在毒理学、药理学和癌症研究中被广泛研究。特别地, NQO2 的多态性 (如 I29T 和 L47F) 与多种药物代谢和疾病易感性相关, 导致群体遗传学研究增加了大量文献。

3. **结构数据极为丰富但非决定因素**: NQO2 拥有本次评估中最卓越的结构数据 -- AlphaFold pLDDT=98.1 (98.3% 残基 pLDDT>90), 72 个 PDB 实验结构 (分辨率 1.20-2.50A)。然而结构维度 (权重 x3, 30 分) 无法弥补研究新颖性 (权重 x5, 50 分) 的 0 分。

4. **蛋白本质是代谢酶, 非染色质/转录调控蛋白**: NQO2 的功能是 quinone reductase (醌还原酶), 属于 II 相解毒酶。虽然 NQO2 在核内也有分布 (nucleoplasm additional), 但其功能与 detoxification 和 vitamin K metabolism 相关, 与 TE 调控 / 染色质调控无关。InterPro 和 Pfam 标注为 Flavodoxin-like fold 和 Flavodoxin_2 结构域, 均为电子传递/氧化还原相关结构域。

**结论**: NQO2 的原始淘汰理由充分。结构数据虽然极为亮眼 (98.1 pLDDT, 72 PDB), 但核定位薄弱 + 研究热度 146 篇 + 代谢酶本质使其不适合作为 TE 调控核蛋白的候选目标。维持 REJECT。

### 3. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Cytosol (主) + Nucleoplasm (额外), Supported; UniProt: Cytoplasm; GO: cytosol (IDA:CAFA) |
| 蛋白大小 | 9/10 | x1 | 9 | 231 aa / 25.9 kDa (理想范围 200-800 aa 近下限) |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=146 篇 (>100 -> 0/10, 一票否决) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=98.1, pct>90=98.3%; PDB: 72 entries (X-ray, 1.20-2.50A) |
| 调控结构域 | 4/10 | x2 | 8 | IPR003680 (Flavodoxin-like), Pfam PF02525 (Flavodoxin_2); 代谢酶结构域, 非调控 |
| PPI 网络 | 3/10 | x3 | 9 | STRING max=0.652 (CRYZ); 全 text-mining/database; IntAct 15 互作 (Y2H 为主) |
| 互证加分 | -- | max +3 | 3.0 | PDB+AF(双源最高质量) + STRING+IntAct + domain+AF + PDB极多条目 |
| **原始总分** | | | **75.0/180** | |
| **归一化总分** | | | **41.7/100** | |

### 4. 详细分析

#### 4.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol (主定位), Nucleoplasm (附加定位) | Supported |
| UniProt subcellular | Cytoplasm (无 evidence code) | Swiss-Prot |
| GO Cellular Component | cytosol (GO:0005829, IDA:CAFA); nucleoplasm (GO:0005654, IDA:HPA); extracellular exosome (GO:0070062, HDA:UniProt) | 3 个实验证据 |

**核定位证据分析**:
- HPA IF: Cytosol 为主, Nucleoplasm 为附加 (additional location)。这意味着在 HPA 的 IF 实验中, 大部分信号在胞质, 核内信号存在但较弱。
- UniProt 仅标注 Cytoplasm (无 evidence code, 可能是历史注释)
- GO-CC 中 cytosol (IDA:CAFA) 的证据级别高于 nucleoplasm (IDA:HPA)
- NQO2 是醌还原酶, 其辅因子 NRH (ribosyldihydronicotinamide) 在胞质中合成, 功能天然偏向胞质
- 核内分布可能反映被动扩散 (231 aa, 25.9 kDa, 接近被动扩散阈值 40-60 kDa) 而非主动核定位

**结论**: 核定位证据薄弱。HPA 将 Nucleoplasm 列为附加定位而非主定位, UniProt 仅列 Cytoplasm。得分维持 4/10。

#### 4.2 蛋白大小评估

| 参数 | 数值 |
|------|------|
| 氨基酸数 | 231 aa |
| 分子量 | 25.9 kDa |
| 理想范围 | 200-800 aa (下限) |

**评价**: 231 aa 刚好在理想范围内 (>200 aa 下限)。小蛋白易表达纯化, 实验操作友好。25.9 kDa 接近被动扩散通过核孔的分子量阈值, 这进一步支持核内分布可能为被动扩散的推断。

#### 4.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 146 |
| PubMed symbol_only count | 246 |
| PubMed broad count | 247 |
| 别名(未计入scoring) | NMOR2 |

**关键文献**:
1. Janda E, Boutin JA, De Lorenzo C et al. (2024). "Polymorphisms and Pharmacogenomics of NQO2: The Past and the Future." *Genes*. PMID: 38254976
2. Rashid MH, Babu D, Tran NH et al. (2025). "The induction of quinone oxidoreductases NQO1 and NQO2 by clozapine: Potential implications for clozapine-induced agranulocytosis." *Toxicology letters*. PMID: 40311769
3. Islam F, Leung KK, Walker MD et al. (2022). "The Unusual Cosubstrate Specificity of NQO2: Conservation Throughout the Amniotes and Implications for Cellular Function." *Frontiers in pharmacology*. PMID: 35517822
4. Long DJ 2nd, Jaiswal AK (2000). "NRH:quinone oxidoreductase2 (NQO2)." *Chemico-biological interactions*. PMID: 11154737
5. Long DJ 2nd, Jaiswal AK (2000). "Mouse NRH:quinone oxidoreductase (NQO2): cloning of cDNA and gene- and tissue-specific expression." *Gene*. PMID: 10903442

**评价**: PubMed 146 > 100, 研究热度维度触犯一票否决 (0/10)。NQO2 在毒理学、药物代谢、群体遗传学 (polymorphisms) 领域研究非常广泛。虽然结构生物学数据极其丰富, 但功能性研究同样大量存在。

#### 4.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 98.1 |
| 高置信度残基 (pLDDT>90) 占比 | 98.3% |
| 置信残基 (pLDDT 70-90) 占比 | 0.9% |
| 中等置信 (pLDDT 50-70) 占比 | 0.9% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.2% |
| 可用 PDB 条目 | 72 个 (X-ray, 分辨率 1.20-2.50A, 覆盖残基 1-231 或 2-231) |

**评价**: 本次 8 个重评基因中结构数据最优。AlphaFold pLDDT=98.1 是近乎完美的预测, 99.2% 残基处于有序状态。72 个 PDB 实验结构, 最高分辨率 1.20A (4FGL), 覆盖多种配体结合状态 (holo/apo, 抑制剂, 辅因子类似物)。NQO2 在结构生物学领域是模式蛋白, 常被用作药物筛选靶点的结构模板。

#### 4.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR003680 (Flavodoxin-like fold), IPR029039 (Flavodoxin-like superfamily), IPR051545 (Quinone reductase 2) |
| Pfam | PF02525 (Flavodoxin_2) |

**染色质调控潜力分析**: NQO2 含有典型的 Flavodoxin-like 结构域, 属于氧化还原酶的 alpha/beta 折叠家族。该结构域负责 FMN/FAD 辅因子结合和电子传递, 与染色质调控、转录调控或表观遗传修饰无已知功能关联。NQO2 是经典的 II 相解毒酶, 其结构域功能仅与代谢解毒相关。

#### 4.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CRYZ | 0.652 | 0 | 醌氧化还原酶同源物 |
| CYP19A1 | 0.640 | 0 | 芳香化酶 |
| TMCO3 | 0.589 | 0.310 | 跨膜蛋白 |
| JMJD7-PLA2G4B | 0.564 | 0.293 | 融合蛋白 |
| ABL1 | 0.541 | 0 | 酪氨酸激酶 |
| IYD | 0.539 | 0 | 碘酪氨酸脱碘酶 |
| LRRC7 | 0.536 | 0.536 | 突触后密度蛋白 |
| PALB2 | 0.503 | 0 | BRCA2 互作蛋白 |
| ARHGEF5 | 0.491 | 0 | RhoGEF |
| B3GAT2 | 0.485 | 0 | 葡萄糖醛酸转移酶 |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GORASP2 | two hybrid pooling | 16189514 |
| SPG21 | validated two hybrid | 32296183 |
| DDIT4L | two hybrid prey pooling | 32296183 |
| LRRC7 | two hybrid array | 32296183 |
| EFHC1 | validated two hybrid | 32296183 |
| EGFR | tandem affinity purification | 24189400 |
| DGCR6 | two hybrid array | 24722188 |
| RELB | tandem affinity purification | 14743216 |
| COPS5 | tandem affinity purification | 21145461 |
| RHOB | two hybrid | 19637314 |

**PPI 互证分析**:
- STRING combined scores 普遍偏低 (max=0.652, 无 >0.7 的 partner)
- 实验验证主要是 yeast two-hybrid (Y2H), 缺乏 co-IP 或 cross-linking 等更可靠的方法
- 互作伙伴功能多样化, 无功能收敛 (代谢、信号、突触后、跨膜蛋白)
- STRING partners: 15, IntAct interactions: 15

**评价**: PPI 网络薄弱。最高 STRING score 仅 0.652 (CRYZ, 完全 text-mining)。IntAct 以 Y2H 为主, 可能存在假阳性。无实验验证的高置信度核心互作伙伴。

#### 4.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=98.1 + PDB 72 entries | pLDDT=98.1, v6, 72 PDB (1.20-2.50A) | 预测+实验 (高度一致) |
| 定位 | UniProt + HPA + GO | Cytoplasm / Cytosol+Nucleoplasm (additional) / cytosol+nucleoplasm | 部分一致 (核内附加定位) |
| PPI | STRING + IntAct | 15 + 15 interactions (Y2H 为主) | 数据存在但质量低 |

**互证加分明细**:
- PDB + AlphaFold 双源验证 (72 实验结构 + 近乎完美预测): +1.0
- 多库定位一致: +0 (HPA 说 Nucleoplasm additional, UniProt 未列核定位, 不完全一致)
- STRING + IntAct 双源验证: +0.5
- 结构域 (Flavodoxin) + AlphaFold 高质量预测一致性: +0.5
- PDB 极多条目覆盖 (72 entries, 远大于 3): +1.0
**总分**: +3.0 / max +3 (结构数据的互证加分达到上限)

### 5. 总体评价

**推荐等级**: REJECT CONFIRMED (原始评估 REJECTED -> 重新评估 REJECTED)

**核心优势**:
1. 结构数据极优: AlphaFold pLDDT=98.1 (本次 8 个基因中最高), 72 个 PDB 实验结构 (最高分辨率 1.20A)
2. 蛋白大小实验友好 (231 aa, 25.9 kDa)
3. NQO2 在结构生物学和药物化学中是成熟的模型系统

**劣势/不确定性**:
1. 核定位薄弱: HPA 将 Nucleoplasm 列为附加定位, UniProt 仅列 Cytoplasm
2. PubMed 146 篇 > 100, 研究热度过高 (0/10, 加权 x5)
3. 功能本质是代谢酶 (quinone reductase), 与 TE 调控/染色质调控无关
4. PPI 网络弱 (STRING max=0.652, Y2H 为主)
5. 25.9 kDa 接近被动扩散阈值, 核内分布可能非主动核定位

**False Rejection 定性**:
原始评估中对 NQO2 的核定位和研究热度判断均正确。虽然该蛋白的结构数据令人印象深刻 (98.1 pLDDT, 72 PDB), 但结构维度的权重 (x3, max 30) 不足以抵消研究新颖性 (x5, max 50) 的 0 分。更重要的是, NQO2 的功能本质与 TE 调控研究的核心目标 (染色质调控、转录调控) 不匹配。核定位的薄弱性进一步支持 REJECT 判定。

**下一步建议**:
- [ ] 如需探索氧化还原与 TE 调控的交叉, 可考虑 NQO2 的转录调控因子 (如 NRF2/NFE2L2) 而非 NQO2 本身
- [ ] NQO2 的 72 个 PDB 结构可用作结构生物学教学/方法学开发
- [ ] NQO2 在药物代谢中的角色可支持药理基因组学方向的独立研究, 但不适合当前的 TE 调控核蛋白筛选

### 6. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P16083
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124588-NQO2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NQO2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P16083
- STRING: https://string-db.org/network/9606.ENSP00000319547
- Data fetched live: 2026-06-02
