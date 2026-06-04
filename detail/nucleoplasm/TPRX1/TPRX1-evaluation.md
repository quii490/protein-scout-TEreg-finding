---
type: protein-evaluation
gene: "TPRX1"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation, scored]
status: scored
_date: 2026-05-29
_notes: "PubMed=12 (<100) → 基线提升: 结2→5, 域5→6; 无HPA IF→核=7; PDB查无结构"
---

## TPRX1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TPRX1 / Tetra-peptide repeat homeobox 1 / TPRX |
| 蛋白大小 | 411 aa / ~46 kDa |
| UniProt ID | Q8N7U7 |
| 评估日期 | 2026-05-28 () / 2026-05-29 |

### 2. 评分总览 (核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | **28** | UniProt+GO预测Nucleus; 无HPA IF; Homeobox TF家族保守→7 |

> **Protein Atlas IF**: 暂无数据（Pending cell analysis），核定位依据 UniProt + GO。

| 📏 蛋白大小 | 10/10 | ×1 | **10** | 411 aa / 46 kDa, 300-800最佳区间 |
|---|---|---|---|---|
| 🆕 研究新颖性 | 10/10 | ×5 | **50** | PubMed=12; 极度新颖 |
| 🏗️ 三维结构 | 5/10 | ×3 | **15** | pLDDT 43.3; 无PDB; 新颖基线5 |
| 🧬 调控结构域 | 6/10 | ×2 | **12** | Homeobox(4库确认); 新颖基线6 |
| 🔗 PPI | 5/10 | ×3 | **15** | DUXA(0.730),NANOGNB(0.681),MBD3L3(0.475); 75%调控相关但text-mining→5 |
| ➕ 互证加分 | — | — | **+1.0** | >=3库结构域互证; DNA-binding一致 |
| **原始总分** |  |  | **131/183** |  |
| **归一化总分** |  |  | **71.6/100** |  |

### 3. PPI 网络分析

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association/direct interaction):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| ATXN1 | Y2H | 32296183 | Ataxin-1, transcription factor | ✅ 转录调控 |
| MKRN3 | Y2H | 32296183 | E3 ubiquitin ligase | ❌ |
| GOLGA2 | Y2H | 32296183 | Golgin | ❌ |
| OIP5 | Y2H | 32296183 | Oncoprotein, mitosis | ❌ |
| FANCG | Y2H | 32296183 | Fanconi anemia | ❌ |
| USHBP1 | Y2H | 32296183 | Usher syndrome binding | ❌ |
| INCA1 | Y2H | 32296183 | Cyclin inhibitor | ❌ |
| GOLGA6L9 | Y2H | 32296183 | Golgin | ❌ |
| KRTAP6-2 | Y2H | 32296183 | Keratin-associated | ❌ |
| KRTAP19-7 | Y2H | 32296183 | Keratin-associated | ❌ |
| PRR20D | Y2H | 32296183 | Proline-rich | ❌ |

> 11 个 IntAct 实验互作全部来自 PMID:32296183 高通量 Y2H。ATXN1 是唯一调控相关 partner (转录因子, SCA1 致病基因)。其余均为结构蛋白或非核蛋白。

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---|---|---|---|
| DUXA | 0.730 | Double homeobox TF (EGA) | ✅ 早期胚胎 TF |
| NANOGNB | 0.681 | Nanog neighbor (多能性) | ✅ 多能性 TF |
| ZNF555 | 0.620 | C2H2 锌指 TF | ✅ 转录调控 |
| DUXB | 0.612 | Double homeobox TF (EGA) | ✅ 早期胚胎 TF |
| LEUTX | 0.557 | Homeobox TF (EGA) | ✅ 早期胚胎 TF |
| DPRX | 0.549 | Homeobox TF (EGA) | ✅ 早期胚胎 TF |
| MBD3L5 | 0.488 | Methyl-CpG binding (EGA) | ✅ 表观遗传 |
| MBD3L3 | 0.475 | Methyl-CpG binding (EGA) | ✅ 表观遗传 |
| ZSCAN4 | 0.466 | Zinc finger, telomere (EGA) | ✅ 染色质 |
| DUX4 | 0.441 | Double homeobox TF (EGA) | ✅ 早期胚胎 TF |
| ARGFX | 0.437 | Homeobox TF | ✅ 转录调控 |
| MBD3L2 | 0.430 | Methyl-CpG binding (EGA) | ✅ 表观遗传 |
| OOEP | 0.424 | Oocyte-expressed protein | ⚠️ |
| ZBED1 | 0.418 | Zinc finger BED-type | ✅ DNA transposase |

**已知复合体成员** (GO Cellular Component / 推断):
- 无已知染色质调控复合体成员身份

**PPI 互证分析**:
- STRING + IntAct 共同确认: **0** (IntAct partners 与 STRING 完全不重叠)
- STRING 预测: 75% 为 EGA 相关 homeobox TF (DUXA, DUXB, LEUTX, DPRX, DUX4) + 表观遗传因子 (MBD3L2/3/5)
- IntAct 实验: 1/11 (9.1%) 调控相关 (ATXN1)
- STRING 调控相关比例: ~75% (12/16, 高度一致指向 EGA 调控网络)

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TPRX1/TPRX1-PAE.png]]

**评价**: TPRX1 的 STRING 预测与 DPRX 高度相似 -- EGA 相关 homeobox TF 网络 + MBD3L 表观遗传因子。IntAct 中 ATXN1 的 Y2H 互作是唯一的调控相关实验线索, 但仅为 Y2H 高通量。STRING 邻居蛋白的一致性极高 (75% 调控相关), 且与 TPRX1 的 EGA 功能完全吻合。评分维持在 **5/10** (无 STRING+IntAct 共同确认的调控 partner, 但 STRING 邻居高度一致指向 EGA)。

### X. 关键文献 (PubMed)

1. Zou Z et al. (2022). "Translatome and transcriptome co-profiling reveals a role of TPRXs in human zygotic genome activation.". *Science*. PMID: 36074823
2. Taubenschmid-Stowers J et al. (2022). "8C-like cells capture the human zygotic genome activation program in vitro.". *Cell Stem Cell*. PMID: 35216671
3. Mazid MA et al. (2022). "Rolling back human pluripotent stem cells to an eight-cell embryo-like stage.". *Nature*. PMID: 35314832
4. Wang Q et al. (2025). "Maternal factor OTX2 regulates human embryonic genome activation and early development.". *Nat Genet*. PMID: 41145868
5. Madissoon E et al. (2016). "Characterization and target genes of nine human PRD-like homeobox domain genes expressed exclusively in early embryos.". *Sci Rep*. PMID: 27412763

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. **极度新颖**: PubMed仅12篇，几乎无功能研究。相比之下 LEUTX 还有50篇
2. **PPI，生殖系/早期发育特异性
3. **中等大小**: 411 aa 在实验上非常友好
4. **高比例调控 partner**: PPI中75%为调控相关蛋白

**风险/不确定性**:
1. **结构质量极差**: 93.6% 无序。AlphaFold 预测对此蛋白几乎不可用，实际结构可能为 folding upon binding
2. **Homeobox 极短**: 仅 22 aa，可能为退化或新型 homeodomain
3. **无实验证据支持**: 无 IF 数据、无 ChIP-seq、无 knock-out 表型
4. **表达量极低**: nTPM 0.1，可能仅限早期胚胎或生殖系

**下一步建议**:
- [ ] 确认 TPRX1 在哪些组织/发育阶段表达（scRNA-seq 数据查询）
- [ ] AlphaFold3 或 ESMFold 重预测（看无序区域是否有改进）
- [ ] 与 DUXA/DUX4 的进化关系和基因组共定位分析
- [ ] 如表达受限，可考虑异位表达实验
- [ ] IDR 区域的相分离预测（如 catGRANULE, PLAAC 等工具）

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N7U7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178928-TPRX1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TPRX1%22
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N7U7
- STRING: https://string-db.org/network/9606.ENSP00000323455


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[TPRX1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TPRX1/TPRX1-PAE.png]]
